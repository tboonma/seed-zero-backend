# Seed: Zero Backend Starter code
This exercise is for Backend session in **Seed: Zero**.   
To make sure you understand the material, there are some requirements:
- Backend is runnable.
- Backend has a top-level endpoint `/`
- Backend can calculate a simple math in the path `/calculator`

## Contribution
### Environment
| Name | Version |
|------|---------|
| Python | 3.9 |

### Installation
#### If you can use GitHub
1. Fork this repository.

2. Clone the project to your local machine. Open a terminal first and go to some directory.
```
git clone https://github.com/{your-github-account}/seed-zero-backend.git
```
3. Go to your cloned directory in your machine
```
cd seed-zero-backend
```
4. use python virtual environment
```
python -m venv venv
```
5. Use the virtual environment
- for MacOS/Linux
```
source venv/bin/activate
```
- for Windows
```
activate
```
6. Install dependencies
```
pip install -r requirements.txt
```
7. Run the app
```
uvicorn main:app --reload
```
8. Edit code in `#TODO` in `app.py`
9. Test whether your code works by open these url in your browser.
- http://localhost:8000/ should display your text
- http://localhost:8000/calculator?first_number=1&second_number=2 should display 3
10. Upload your work
```
git add .
git commit -m "Finish work"
git push
```
11. Open Pull Request in this repository.
12. Go to your opened Pull Request and click the link in comment.

#### If you cannot use GitHub
1. Download this project as zip in the green button with text "Code", select **Download ZIP**.
![Screen Shot 2565-08-27 at 20 51 13](https://user-images.githubusercontent.com/63687258/187033193-ad69b346-cc9e-4fb5-b1fa-b124a72fbcfd.png)
2. Extract file and open a terminal in the project's directory.
use python virtual environment
```
python -m venv venv
```
3. Use the virtual environment
- for MacOS/Linux
```
source venv/bin/activate
```
- for Windows
```
activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Run the app
```
uvicorn main:app --reload
```
6. Edit code in `#TODO` in `app.py`
7. Test whether your code works by open these url in your browser.
- http://localhost:8000/ should display your text
- http://localhost:8000/calculator?first_number=1&second_number=2 should display 3
8. Finish!
