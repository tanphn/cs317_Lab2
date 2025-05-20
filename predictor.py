import torch
import torchvision.models as models
from torchvision.models import ResNet18_Weights
import torchvision.transforms as transforms
from PIL import Image

# 1. Khởi tạo kiến trúc ResNet18 (6 lớp đầu ra)
model = models.resnet18(weights=None)
num_classes = 6
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

# 2. Load trọng số đã huấn luyện
model.load_state_dict(torch.load("model/best_model.pt", map_location="cpu"))

# 3. Chuyển về chế độ eval để inference
model.eval()

# 4. Tiền xử lý ảnh đầu vào
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# 5. Mapping nhãn
class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

# 6. Hàm dự đoán tên lớp từ ảnh
def predict_image(image: Image.Image):
    img_t = transform(image).unsqueeze(0)  # thêm batch dimension
    with torch.no_grad():
        output = model(img_t)
    pred = torch.argmax(output, 1).item()
    return class_names[pred]

# 7. Ví dụ sử dụng
if __name__ == "__main__":
    # Đường dẫn ảnh đầu vào
    image_path = "path/to/your/image.jpg"
    image = Image.open(image_path).convert("RGB")
    
    prediction = predict_image(image)
    print("Predicted class:", prediction)
