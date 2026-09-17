from flask import Flask

app = Flask(__name__)


def page_layout(title, content):
    return f"""
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h1>{title}</h1>
            {content}
            <p>
                <a href="/">Home</a> |
                <a href="/about">About</a> |
                <a href="/courses">Courses</a> |
                <a href="/contact">Contact</a>
            </p>
        </body>
    </html>
    """


@app.route("/")
def home():
    content = """
        <p>Welcome to Student Portal.</p>
        <p>This portal is designed to help students learn about our programs, campus services, and support team.</p>
        <p>Students can explore course options and get basic information quickly.</p>
    """
    return page_layout("Student Portal", content)


@app.route("/about")
def about():
    content = """
        <p>We are here to provide quality education and excellent student support.</p>
        <p>Our mission is to help students grow academically and professionally through guidance, learning, and opportunity.</p>
        <p>We focus on knowledge, discipline, and success for every student.</p>
    """
    return page_layout("About Us", content)


@app.route("/courses")
def courses():
    content = """
        <p>Available programs include:</p>
        <ul>
            <li>BCA</li>
            <li>BSc CS+DS</li>
            <li>MSc DS</li>
            <li>BSc ES</li>
            <li>MBA</li>
            <li>BBA</li>
            <li>BCom</li>
            <li>BA LLB</li>
            <li>BBA LLB</li>
        </ul>
        <p>These courses are designed to build strong academic and career foundations.</p>
    """
    return page_layout("Courses", content)


@app.route("/contact")
def contact():
    content = """
        <p>Email: sysadmin@christuniversity.in</p>
        <p>Phone: +91 00000 00000</p>
        <p>Office Hours: Monday to Saturday, 9:00 AM to 5:00 PM</p>
        <p>For student support, admissions, and general help, contact the support team anytime during working hours.</p>
    """
    return page_layout("Contact Us", content)


if __name__ == "__main__":
    app.run(debug=True)