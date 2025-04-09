from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def clarify_question(query_text):
    prompt = f"""Bạn là một trợ lý AI chuyên xử lý ngôn ngữ tự nhiên. Nhiệm vụ của bạn là chuẩn hóa câu hỏi tiếng Việt từ dạng tự nhiên, không chính thức hoặc lặp từ thành dạng câu hỏi rõ ràng, ngắn gọn, đúng ngữ pháp và giữ nguyên ý nghĩa gốc. Hãy thực hiện các bước sau:

1. Loại bỏ các từ thừa như "dạ", "ạ", "cho em hỏi", "mình", "vậy", "với" khi không cần thiết.
2. Sửa lỗi chính tả, viết hoa đầu câu và các danh từ riêng (nếu có).
3. Chuyển câu thành dạng chuẩn, mạch lạc, không lặp ý.
4. Giữ nguyên nội dung và ý nghĩa của câu hỏi.

Dưới đây là ví dụ:  
- Câu gốc: "Dạ cho e hỏi HUIT và DCT là 1 đúng không"  
- Câu chuẩn hóa: "HUIT và DCT là một đúng không?"

Bây giờ, hãy chuẩn hóa câu hỏi sau:  

"{query_text}"
"""
    response = client.chat.completions.create(
        model=OPENAI_MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

def choose_best_match(clarified_question, retrieved_questions):
    question_list_text = "\n".join([f"STT {stt}: {q}" for stt, q in retrieved_questions])
    prompt = f"""Bạn là một trợ lý AI hiểu tiếng Việt. 
Dưới đây là một câu truy vấn gốc và danh sách 5 câu hỏi gần nhất. 
Nhiệm vụ của bạn là chọn ra một câu hỏi trong danh sách có ý nghĩa gần nhất với câu truy vấn gốc. 

Câu truy vấn gốc: '{clarified_question}'

Danh sách câu hỏi:\n{question_list_text}

Chỉ trả về duy nhất số nguyên là STT tương ứng của câu hỏi phù hợp nhất, không thêm bất kỳ ký tự hoặc từ nào khác như 'STT', dấu chấm hay giải thích.
Nếu trong 5 câu hoàn toàn không có câu nào giống, trả về 'x' nhé
"""
    response = client.chat.completions.create(
        model=OPENAI_MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()
