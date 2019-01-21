# Canvas 1
from IPython.display import display, HTML, clear_output

disp_objects = [{"id":0,"shape":"None","x":0,"y":0,"width":0,"height":0,"kw":None}]
height = 500
width = 800

def _rect(o):
        out = ""
        if o["kw"]["strokeWidth"] > 0:
                out += "ctx.beginPath();\n"
                out += "ctx.lineWidth = \"" + str(o["kw"]["strokeWidth"]) + "\";\n"
                out += "ctx.strokeStyle = \"" + o["kw"]["strokeStyle"] + "\";\n"
                out += "ctx.rect(" + str(o["x"]) + "," + str(o["y"]) + ","+ str(o["width"]) + "," + str(o["height"]) + ");\n"
                out += "ctx.stroke();\n"
        out += "ctx.fillStyle = \"" + o["kw"]["fillstyle"] + "\";\n"
        out += "ctx.fillRect(" + str(o["x"]) + "," + str(o["y"]) + ","+ str(o["width"]) + "," + str(o["height"]) + ");\n"
        return out

def _text(o):
        out = "ctx.fillStyle = \"" + o["kw"]["fillstyle"] + "\";\n"
        out += "ctx.font = \"" + o["kw"]["font"] + "\";\n"
        out += "ctx.fillText(\""+ o["kw"]["text"] +"\", "+ str(o["x"]) +", "+ str(o["y"]) +"); \n"
        return out

def _line(o):
        out = "ctx.beginPath();\n"
        out += "ctx.lineWidth = \"" + str(o["kw"]["strokeWidth"]) + "\";\n"
        out += "ctx.strokeStyle = \"" + o["kw"]["strokeStyle"] + "\";\n"
        out += "ctx.moveTo("+ str(o["x1"]) +", "+ str(o["y1"])+"); \n"
        out += "ctx.lineTo("+ str(o["x2"]) +", "+ str(o["y2"])+"); \n"
        out += "ctx.stroke();\n"
        return out



def _nhandle(o):
        return ""

renderers = {"rect":_rect,"text":_text,"None":_nhandle,"line":_line}
top = True


def _getlargestid():
        global disp_objects
        max = 0
        for obj in disp_objects:
                if int(obj["id"]) > max:
                        max = int(obj["id"])
        return max

def _getobyid(id):
        global disp_objects
        for o in disp_objects:
                if o["id"] == id:
                        return o
        return None

def _rendercanvas():
        global disp_objects,width,height,renderers
        script = "var canvas = document.getElementById(\"myCanvas\");\nvar ctx = canvas.getContext(\"2d\");\n"
        disp_objects = sorted(disp_objects,key = lambda x:x["id"],reverse=False)
        for obj in disp_objects:
                script += renderers[obj["shape"]](obj)
        html = "<script class=\"remove\">" + script + "</script>"
        return html

def _display(script):
        if top:
                canvas = "<canvas id=\"myCanvas\" width=\"" + str(width) + "\" height=\"" + str(height) + "\"></canvas>"
                display(HTML("<script class=\"remove\">document.getElementById(\"myCanvas\").parentElement.parentElement.remove();\nvar x = document.getElementsByClassName(\"remove\")\nvar i;for (i = 0; i < x.length; i++) {x[i].parentElement.parentElement.remove();} </script>"))
                display(HTML(canvas + script))
        else:
                display(HTML("<script class=\"remove\">var x = document.getElementsByClassName(\"remove\");var i;for (i = 0; i < x.length; i++) {x[i].parentElement.parentElement.remove();} </script>"))
                display(HTML(script))
                

def create_new_canvas():
        canvas = "<canvas id=\"myCanvas\" width=\"" + str(width) + "\" height=\"" + str(height) + "\"></canvas>"
        display(HTML("<script class=\"remove\">document.getElementById(\"myCanvas\").parentElement.parentElement.remove();\nvar x = document.getElementsByClassName(\"remove\")\nvar i;for (i = 0; i < x.length; i++) {x[i].parentElement.parentElement.remove();} </script>"))
        display(HTML(canvas))

def _rect_kwords(**kw):
        out = {}
        if "fill" in kw:
                out["fillstyle"] = kw["fill"]
        else:
                out["fillstyle"] = "#000000"
        if "width" in kw:
                out["strokeWidth"] = kw["width"]
        else:
                out["strokeWidth"] = 1
        if "outline" in kw:
                out["strokeStyle"] = kw["outline"]
        else:
                out["strokeStyle"] = "black"
        return out

def create_rectangle(x1,y1,x2,y2, **kw):
        global disp_objects
        if x1 < x2 and y1 < y2:
                width = x2-x1
                height = y2-y1
                kwords = _rect_kwords(**kw)
                disp_objects.append({"id":int(_getlargestid()) + 1,"shape":"rect","x":x1,"y":y1,"width":width,"height":height,"kw":kwords})
                _display(_rendercanvas())
        else:
                width = x1-x2
                height = y1-y2
                kwords = _rect_kwords(**kw)
                disp_objects.append({"id":int(_getlargestid()) + 1,"shape":"rect","x":x2,"y":y2,"width":width,"height":height,"kw":kwords})
                _display(_rendercanvas())

def _text_kwords(**kw):
        out = {}
        out["text"] = kw["text"]
        if "font" in kw:
                out["font"] = kw["text"]
        else:
                out["font"] = "16px Arial"
        if "fill" in kw:
                out["fillstyle"] = kw["fill"]
        else:
                out["fillstyle"] = "#000000"
        return out

def create_text( x1, y1, **kw ):
        global disp_objects
        kwords = _text_kwords(**kw)
        disp_objects.append({"id":int(_getlargestid()) + 1,"shape":"text","x":x1,"y":y1,"width":-1,"height":-1,"kw":kwords})
        _display(_rendercanvas())

def _line_kwords(**kw):
        out = {}
        if "width" in kw:
                out["strokeWidth"] = kw["width"]
        else:
                out["strokeWidth"] = 1
        if "outline" in kw:
                out["strokeStyle"] = kw["outline"]
        else:
                out["strokeStyle"] = "black"
        return out

def create_line(xStart, yStart, xEnd, yEnd,**kw):
        global disp_objects
        kwords = _line_kwords(**kw)
        disp_objects.append({"id":int(_getlargestid()) + 1,"shape":"line","x1":xStart,"y1":yStart,"x2":xEnd,"y2":yEnd,"kw":kwords})
        _display(_rendercanvas())


def clear():
        global disp_objects
        disp_objects = [{"id":0,"shape":"None","x":0,"y":0,"width":0,"height":0,"kw":None}]
        
def complete():
        clear()
        print("Complete")

# def create_rectangle( x1, y1, x2, y2, **kw ):
#     return _getCanvas().create_rectangle( x1, y1, x2, y2, kw )
# def create_arc( x1, y1, x2, y2, **kw ):
#     return _getCanvas().create_arc( x1, y1, x2, y2, kw )
# def create_line( x1, y1, x2, y2, **kw ):
#     return _getCanvas().create_line( x1, y1, x2, y2, kw )
# def create_oval( x1, y1, x2, y2, **kw ):
#     return _getCanvas().create_oval( x1, y1, x2, y2, kw )
# def create_text( x1, y1, **kw ):
#     return _getCanvas().create_text( x1, y1, kw )
# def move( tagOrId, xInc, yInc ):
#     _getCanvas().move( tagOrId, xInc, yInc )
# def wait( t1 ):
#     time.sleep( t1 )
# def delete( tagOrId ):
#     _getCanvas().delete( tagOrId )
# def set_title( txt ):
#     _getCanvas().set_title( txt )
# def set_size( x, y ):
#     _getCanvas().set_size( x, y )
# def complete( a = None ):
#     _getCanvas().complete( a )
# def run():
#     _getCanvas().run()
# def quitCanvas():
#     _getCanvas().quitCanvas()
# def runGraphicsFn( g ):
#     _getCanvas().runGraphicsFn( g )
# def set_keydown_handler( handler ):
#     _getCanvas().set_keydown_handler( handler )
# def unset_keydown_handler():
#     _getCanvas().unset_keydown_handler()
# def set_mousedown_handler( handler ):
#     _getCanvas().set_mousedown_handler( handler )
# def unset_mousedown_handler( handler ):
#     _getCanvas().unset_mousedown_handler()
# def set_mouseup_handler( handler ):
#     _getCanvas().set_mouseup_handler( handler )
# def unset_mouseup_handler():
#     _getCanvas().unset_mouseup_handler()
# def set_mousemotion_handler( handler ):
#     _getCanvas().set_mousemotion_handler( handler )
# def unset_mousemotion_handler():
#     _getCanvas().unset_mousemotion_handler()
# def end_x( start_x, length, angle ):
#     return start_x + length * math.sin( math.radians( angle ) )
# def end_y( start_y, length, angle ):
#     return start_y + length * math.cos( math.radians( angle ) )
