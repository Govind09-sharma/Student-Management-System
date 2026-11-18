from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "student_management_secret_key"


def init_db():
    conn = sqlite3.connect("students.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT NOT NULL UNIQUE,
            email TEXT,
            course TEXT
        )
    """)
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    conn = sqlite3.connect("students.db")

    total_students = conn.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    total_courses = conn.execute(
        "SELECT COUNT(DISTINCT course) FROM students WHERE course != ''"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        total_students=total_students,
        total_courses=total_courses
    )


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        roll_number = request.form.get("roll_number", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not roll_number:
            flash("Name and Roll Number are required.")
            return redirect(url_for("add_student"))

        conn = sqlite3.connect("students.db")

        try:
            conn.execute(
                """INSERT INTO students
                   (name, roll_number, email, course)
                   VALUES (?, ?, ?, ?)""",
                (name, roll_number, email, course)
            )
            conn.commit()
            flash("Student added successfully!")
        except sqlite3.IntegrityError:
            flash("This Roll Number already exists.")
        finally:
            conn.close()

        return redirect(url_for("add_student"))

    return render_template("add_student.html")

@app.route("/students")
def view_students():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row

    students = conn.execute(
        "SELECT * FROM students ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template("students.html", students=students)

@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()

    flash("Student deleted successfully!", "success")
    return redirect(url_for("view_students"))
@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row

    if request.method == "POST":
        name = request.form["name"]
        roll_number = request.form["roll_number"]
        email = request.form["email"]
        course = request.form["course"]

        conn.execute(
            """UPDATE students
               SET name = ?, roll_number = ?, email = ?, course = ?
               WHERE id = ?""",
            (name, roll_number, email, course, student_id)
        )
        conn.commit()
        conn.close()

        flash("Student updated successfully!", "success")
        return redirect(url_for("view_students"))

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()
    conn.close()

    if student is None:
        flash("Student not found!", "error")
        return redirect(url_for("view_students"))

    return render_template("edit_student.html", student=student)
@app.route("/search")
def search_student():
    query = request.args.get("q", "").strip()

    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row

    students = conn.execute(
        """SELECT * FROM students
           WHERE name LIKE ?
           OR roll_number LIKE ?
           ORDER BY id DESC""",
        (f"%{query}%", f"%{query}%")
    ).fetchall()

    conn.close()

    return render_template(
        "students.html",
        students=students,
        search_query=query
    )
if __name__ == "__main__":
    app.run(debug=True)