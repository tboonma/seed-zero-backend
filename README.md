# Seed: Zero Backend Starter code
This exercise is for Backend session in Seed: Zero.   
To make sure you understand the material, there are some requirements:
- Backend is runnable.
- Backend has endpoint named `/seed/zero`
- Backend can calculate a simple math in the path `/math`

## Contribution
### Environment
| Name | Version |
|------|---------|
| Python | 3.9 |

### Installation
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
5. Install dependencies
```
pip install -r requirements.txt
```
6. Run the app
```
uvicorn main:app --reload
```
7. Edit code in `#TODO`
8. Test whether your code works by open these url in your browser.
- http://localhost:5500/seed/zero should display your text
- http://localhost:5500/math/1/2 should display 3
9. Upload your work
```
git add .
git commit -m "Finish work"
git push
```
10. Open Pull Request in this repository.
11. Go to your opened Pull Request and click the link in comment.
