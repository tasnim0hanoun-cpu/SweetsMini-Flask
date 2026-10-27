
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

recipes = [
    {"id": 1, "name": "Chocolate Cake", "description": "A delicious chocolate cake"},
    {"id": 2, "name": "Croissants", "description": "Buttery French pastries"},
    {"id": 3, "name": "Carrot Cake", "description": "A soft carrot cake"}
]

next_id = 4

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sweets Mini</title>
    <style>
        body { font-family: Arial; background: #fff8f5; margin: 0; color: #62464d; }
        header { background: #ef90ac; padding: 25px; text-align: center; color: white; }
        main { max-width: 850px; margin: 35px auto; padding: 20px; }
        .card { background: white; padding: 20px; margin: 15px 0; border-radius: 12px; box-shadow: 0 2px 8px #ddd; }
        input { padding: 12px; margin: 5px; border: 1px solid #ddd; border-radius: 6px; }
        button, .btn { background: #e9789b; color: white; border: none; padding: 10px 16px; border-radius: 6px; cursor: pointer; text-decoration: none; }
        .delete { background: #cc4b60; }
        h2 { color: #704e58; }
    </style>
</head>
<body>
    <header>
        <h1>Sweets Mini</h1>
        <p>Recipe Management with Python Flask</p>
    </header>
    <main>
        <div class="card">
            <h2>Add New Recipe</h2>
            <form action="/add" method="post">
                <input name="name" placeholder="Recipe name" required>
                <input name="description" placeholder="Description" required>
                <button type="submit">Add Recipe</button>
            </form>
        </div>

        <h2>All Recipes</h2>
        {% for recipe in recipes %}
        <div class="card">
            <h3>{{ recipe.name }}</h3>
            <p>{{ recipe.description }}</p>
            <a class="btn" href="/edit/{{ recipe.id }}">Edit</a>
            <form action="/delete/{{ recipe.id }}" method="post" style="display:inline">
                <button class="delete" type="submit">Delete</button>
            </form>
        </div>
        {% endfor %}
    </main>
</body>
</html>
"""

EDIT_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Edit Recipe</title>
    <style>
        body { font-family: Arial; background: #fff8f5; padding: 50px; }
        form { background: white; padding: 30px; max-width: 500px; margin: auto; border-radius: 12px; }
        input { display: block; width: 95%; padding: 12px; margin: 15px 0; }
        button { background: #e9789b; color: white; padding: 12px 20px; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <form method="post">
        <h2>Edit Recipe</h2>
        <input name="name" value="{{ recipe.name }}" required>
        <input name="description" value="{{ recipe.description }}" required>
        <button type="submit">Save Changes</button>
        <a href="/">Cancel</a>
    </form>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(PAGE, recipes=recipes)


@app.route("/add", methods=["POST"])
def add_recipe():
    global next_id
    name = request.form["name"].strip()
    description = request.form["description"].strip()

    if name and description:
        recipes.append({
            "id": next_id,
            "name": name,
            "description": description
        })
        next_id += 1

    return redirect("/")


@app.route("/edit/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)

    if recipe is None:
        return "Recipe not found", 404

    if request.method == "POST":
        recipe["name"] = request.form["name"].strip()
        recipe["description"] = request.form["description"].strip()
        return redirect("/")

    return render_template_string(EDIT_PAGE, recipe=recipe)


@app.route("/delete/<int:recipe_id>", methods=["POST"])
def delete_recipe(recipe_id):
    global recipes
    recipes = [r for r in recipes if r["id"] != recipe_id]
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
