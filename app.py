from flask import Flask,render_template , request
import requests 

app = Flask(__name__)

@app.route("/")
def home():

   return render_template("index.html")

@app.route("/analyze",methods=["POST"])

def analyze():
    username= request.form["username"]

    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return "User not found"

    repos= response.json()
    total_repos = len(repos)

    # ✅ YE SAB ANDAR HONA CHAHIYE
    language_count = {}

    for repo in repos:
        lang = repo.get("language")

        if lang:
            if lang in language_count:
                language_count[lang] += 1
            else:
                language_count[lang] = 1

    top_language = None
    if language_count:
        top_language = max(language_count, key=language_count.get)

    score = 0

    if total_repos > 5:
        score += 1
    if total_repos > 10:
        score += 1
    if top_language:
        score += 1

    if score == 1:
        skill_level = "Beginner"
    elif score == 2:
        skill_level = "Intermediate"
    else:
        skill_level = "Advanced"
    
    # ✅ RETURN HAMESHA END ME
    return render_template(
        "Result.html",
        username=username,
        total_repos=total_repos,
        languages=language_count,
        top_language=top_language,
        skill_level=skill_level
    )
if __name__ == "__main__":
    app.run(debug=True)
    