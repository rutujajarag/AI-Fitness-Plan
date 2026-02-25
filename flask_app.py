from gemini_connect import create_prompt,get_response
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_ai_fitness_plane():
    if request.method == "POST":
        fitness_goal = request.form.get("fitness_goal")
        workout_per_week=request.form.get("workout_per_weak")
        minutes_per_day=request.form.get("minutes_per_day")
        diet_preference=request.form.get("diet_preference")
        ai_prompt=create_prompt(fitness_goal,workout_per_week,minutes_per_day,diet_preference)
        ai_response=get_response(ai_prompt)
        return render_template("fitness_plan_result.html",ans= ai_response)

    return render_template ('generate_ai_fitness_plan.html')

if __name__ == "__main__":
    app.run(debug=True)