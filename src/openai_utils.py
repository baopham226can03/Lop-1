from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def clarify_question(query_text):
    prompt = f"""Bạn là một chuyên gia về ngôn ngữ tiếng Việt. Đang ở ngữ cảnh là hỏi đáp các vấn đề của trường Đại học Công Thương TPHCM. 
Hãy chuyển đổi câu hỏi sau thành một câu hỏi rõ ràng, đầy đủ ngữ pháp, thể hiện đầy đủ mục đích của người hỏi.
Nếu câu hỏi quá ngắn hoặc mơ hồ như “học phí?”, “ngành?”, “ngập học?” thì hãy viết lại thành các câu như “Học phí của trường là bao nhiêu?”, “Trường có những ngành đào tạo nào?”, “Thủ tục nhập học như thế nào?”.
Khi câu hỏi không được rõ ràng, lang mang, không có mục đích thì cũng viết lại trình bày lại cho đẹp.
Ngoài ra câu hỏi cũng phải ở dạng đơn giản nhất có thể, đừng đi quá cụ thể nêu
Chỉ trả về duy nhất câu hỏi đã được chuyển đổi, không thêm bất kỳ nhận xét hay giải thích nào.


Câu hỏi gốc: "{query_text}"
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
Nếu trong 5 câu hoàn toàn không có câu nào giống, trả về 'x' nhé, tuyển chọn gắt gao chỉ chọn khi ý nghĩa thật sự giống, không khoan nhượng nhé
"""
    response = client.chat.completions.create(
        model=OPENAI_MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()
