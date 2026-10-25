from flask import Flask, request, render_template_string


app = Flask(__name__)

students = []


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form.get("name")
        register_number = request.form.get("register_number")
        course = request.form.get("course")

        if name and register_number and course:
            students.append({
                "name": name,
                "register_number": register_number,
                "course": course
            })
            message = "Student information submitted successfully."
        else:
            message = "Please fill all fields."

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Information App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            input { display: block; margin: 8px 0 15px; padding: 8px; width: 260px; }
            button { padding: 8px 16px; }
        </style>
    </head>
    <body>
        <h1>Student Information App</h1>
        <form method="post">
            <label>Student Name</label>
            <input type="text" name="name">

            <label>Register Number</label>
            <input type="text" name="register_number">

            <label>Course</label>
            <input type="text" name="course">

            <button type="submit">Submit</button>
        </form>

        <p><b>{{ message }}</b></p>

        <h2>Submitted Students</h2>
        {% if students %}
            <ul>
            {% for student in students %}
                <li>{{ student.name }} - {{ student.register_number }} - {{ student.course }}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No student information submitted yet.</p>
        {% endif %}
    </body>
    </html>
    """, message=message, students=students)


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
