import spacy
import cv2

# leonardo.Ai
# تحميل مكتبة اللغة العربية
nlp = spacy.blank("ar")

# قاعدة بيانات الإشارات
signal_database = {
    "نحلة": r"D:\asd\ArabicToSignLanguage\data\signals\nahla.mp4",
    "غزالة": r"D:\asd\ArabicToSignLanguage\data\signals\gazal.mp4",
    "كلب": r"D:\asd\ArabicToSignLanguage\data\signals\kalb.mp4",
    "فيل": r"D:\asd\ArabicToSignLanguage\data\signals\feel.mp4",
    "أهلاً": r"D:\asd\ArabicToSignLanguage\data\signals\ahlan.mp4",
    "بك": r"D:\asd\ArabicToSignLanguage\data\signals\bika.mp4",
    "لغة": r"D:\asd\ArabicToSignLanguage\data\signals\logha.mp4",
    "الإشارة": r"D:\asd\ArabicToSignLanguage\data\signals\eshara.mp4"
}

# وظيفة لتحليل النص وترجمته
def translate_text_to_signs(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.text in signal_database]
    return [signal_database[word] for word in keywords]

# وظيفة تشغيل الفيديو
def play_video(video_path):
    print(f"تشغيل الفيديو: {video_path}")  # طباعة مسار الفيديو للتأكد
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"خطأ: لا يمكن فتح الفيديو {video_path}")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        # تأخير بسيط حتى لا يغلق الفيديو بسرعة
        if cv2.waitKey(20) & 0xFF == ord('q'):  # 30 هو التأخير بالميللي ثانية
            break

    cap.release()
    cv2.destroyAllWindows()

# البرنامج الرئيسي
if __name__ == "__main__":
    input_text = input("أدخل النص الذي تريد ترجمته إلى لغة الإشارة: ")
    result = translate_text_to_signs(input_text)

    if result:
        print("الإشارات المطلوبة:", result)
        # تشغيل الفيديوهات بالتتابع
        for video in result:
            play_video(video)
    else:
        print("لا توجد إشارات متوفرة للنص المدخل.")
