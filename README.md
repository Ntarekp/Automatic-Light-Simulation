# 🌌 CyberLight Control v1.0

A cyberpunk-themed MQTT-based light control system simulation with virtual IoT device.

![CyberLight Interface Preview]([https://via.placeholder.com/800x500.png?text=CyberLight+Control+Interface](https://github.com/Ntarekp/Automatic-Light-Simulation/blob/main/preview/Screenshot%202025-03-14%20115019.png))

## 🚀 Features
- **Cyberpunk Web Interface** with neon aesthetics
- MQTT-based light control simulation
- Virtual IoT device (Python)
- Particle animations & dynamic status updates
- Responsive design with hover effects

## 📦 Prerequisites
- Python 3.8+
- Modern web browser
- Internet connection (for MQTT broker)

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/Ntarekp/Automatic-Light-Simulation.git
cd Automatic-Light-Simulation
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install paho-mqtt
```

## 🖥️ Usage

### Start Virtual IoT Device
```bash
python light_simulation.py
```

### Open Web Interface
1. Open `index.html` in a modern browser
2. Click buttons to control light status:
   - 🔵 **ACTIVATE LUMINESCENCE** (ON)
   - 🔴 **INITIATE DARKNESS** (OFF)

### Expected Output (Python Terminal)
```
💡 CYBERLIGHT ACTIVATED [STATUS: LUMINESCENT]
🌑 DARKNESS PROTOCOL ENGAGED [STATUS: INACTIVE]
```

## 📂 File Structure
```
Automatic-Light-Simulation/
├── index.html            # Cyberpunk web interface
├── light_simulation.py   # Virtual IoT device
├── README.md             # Project documentation
└── venv/                 # Virtual environment
```

## 🔧 Customization
- **MQTT Topics**: Edit in both files:
  ```javascript
  // index.html
  client.publish('/student_group/light_control', 'ON')
  ```
  ```python
  # light_simulation.py
  TOPIC = "/student_group/light_control"
  ```

## 🚨 Troubleshooting
- **Pip Errors**: Use virtual environment
- **Connection Issues**: Verify MQTT broker status
- **Style Issues**: Clear browser cache

## 📄 License
MIT License - Free for modification and distribution

## 📧 Contact
Email: [kpntare@gmail.com](mailto:kpntare@gmail.com)  
Project Link: [GitHub Repo](https://github.com/Ntarekp/Automatic-Light-Simulation)
```
