from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

story_types_dict = {
  "silly_story": silly_story,
  "excited_story": excited_story
}

@app.get('/<story_type>')
def send_story_prompts(story_type):
  """ get the story prompts form """

  try: 
    s = story_types_dict[story_type]
    prompts = s.prompts

    if story_type in story_types_dict:
      return render_template("questions.html", prompts = prompts, 
      story_type = story_type)

  except:
    return f"{story_type} route does not exist!"

@app.post('/<story_type>')
def handle_story_submit(story_type):
  """ create the story from the template and prompts """

  s = story_types_dict[story_type]

  inputs = [(key, value) for (key, value) in request.form.items()]
  
  # create story using template
  story = s.generate(inputs)

  return render_template("results.html", story)


@app.get('/results')
def send():
  return render_template("results.html")



