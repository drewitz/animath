import subprocess as sp
import json

print("""
      ACHTUNG!
      This doesn't work as intended.
      Only dummy calls.
      """)
vid_data = []

with open("slides.json") as f:
    scenes = json.load(f)
    for s in scenes:
        file = s["source_file"]
        slide = s["slides_name"]
        print(sp.list2cmdline(["manim", "render", "py/" + file, slide]))
        #sp.run(["manim", "render", "py/" + file, slide], shell=True)
        print(sp.list2cmdline(["manim-slides", "convert", "-ccontrols=true", slide, "docs/slides/" + slide + ".html"]))
        #sp.run(["manim-slides", "convert", "-ccontrols=true", slide, "docs/slides/" + slide + ".html"], shell=True)
        vid_data.append(
                {
                    "title": slide,
                    "filename": slide + ".html",
                    "path": "slides/"
                }
         )

    #with open("docs/vid_data.js", "w") as new_f:
    #    new_f.write("vid_data = ")
    #    json.dump(vid_data, new_f)




