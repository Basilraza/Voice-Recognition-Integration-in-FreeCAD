# Voice-Controlled BIM Automation in FreeCAD

## Overview

This project demonstrates how voice recognition can be integrated with FreeCAD to automate basic modeling tasks. The aim is to explore the feasibility of using speech as an interface in BIM workflows, enabling users to control modeling operations via voice commands.

---

## 1. Set-up

In this section, we outline the basic setup required to create macros in FreeCAD for voice recognition integration.

### Step 1: Activate the Python Console

* Go to the **View** option in the toolbar.
* Under **Panels**, check both the **Python console** and **Report view** options.

### Step 2: Create a Macro

1. Click on **Macro** in the toolbar and select **Macros**.
2. In the window that appears, click on **Create**, then assign a name to your macro.
3. This will open the macro editor, where you can write your script.

### Step 3: Write the Macro Script

In the macro editor:

* Import required libraries like `speech_recognition` and `pyttsx3`.
* Set up the voice recognition logic and any TTS output.

### Step 4: Add the Macro to the Toolbar

* Right-click on the ribbon and select **Customize**.
* Switch to the **Macros** tab and select your macro.
* Choose an icon and click **Add**.
* Go to the **Toolbar** tab and add your macro to the toolbar.

Once your macro appears as an icon on the toolbar, you can activate voice recognition by clicking the icon. This effectively functions as a “run” button for your script.

---

## 2. Automated Modeling Tasks Achievable via Voice Commands

> **Disclaimer:** These tasks serve as proofs of concept. They were tested using individual code snippets in FreeCAD’s Python console and not integrated into a unified macro file. Full integration would require advanced coding and macro design.

### 1. Adding New Elements

**Voice command:** “Draw me a column.”

* Recognizes keywords like `draw` and `column`.
* Code block:

```python
s = Arch.makeStructure(length=200.0, width=200.0, height=3000)
s.Placement.Base = FreeCAD.Vector(0, 0, 0)
wp = WorkingPlane.get_working_plane()
s.Placement.Rotation = s.Placement.Rotation.multiply(wp.get_placement().Rotation)
Draft.autogroup(s)
App.activeDocument().recompute(None, True, True)
```

### 2. Updating the Dimension of an Element

**Voice command:** “Change the second column height to 3 meters.”

* Example logic:

```python
FreeCAD.getDocument('Unnamed').getObject('Structure002').Height = '3000 mm'
```

### 3. Moving an Element

**Voice command:** “Move column 1 position to 300 300 0.”

```python
FreeCAD.getDocument('Unnamed').getObject('Structure001').Placement = App.Placement(App.Vector(300, 300, 0), App.Rotation(App.Vector(0, 0, 1), 0))
```

### 4. Making Sketches

**Voice command:** “Draw a line of 10 units.”

```python
doc = App.newDocument("SingleLineDoc")
sketch = doc.addObject('Sketcher::SketchObject', 'SingleLineSketch')
line = Part.LineSegment(App.Vector(0, 0, 0), App.Vector(10, 0, 0))
sketch.addGeometry(line, False)
doc.recompute()
```

### 5. Changing Views

**Voice command:** “Change the view to isometric.”

```python
Gui.runCommand('Std_ViewGroup', 0)
```

Values:

* 0 – Isometric
* 1 – Front
* 2 – Top
* 3 – Right
* 4 – Rear
* 5 – Bottom
* 6 – Left

### 6. Merging / Adding Elements

**Voice command:** “Merge Wall 1 and Wall 2.”

```python
Gui.Selection.addSelection('Unnamed', 'Wall001')
Gui.Selection.addSelection('Unnamed', 'Wall002')
Arch.addComponents([FreeCAD.ActiveDocument.Wall], FreeCAD.ActiveDocument.Wall002)
```

### 7. Measuring

**Voice command:** “Measure area of Wall 1, Face 1 at coordinate 0,0,0.”

```python
Gui.Selection.addSelection('Unnamed', 'Wall001', 'Face1', 0, 0, 0)
Gui.runCommand('Std_Measure', 0)
```

### 8. Changing and Creating Material

#### A. Semi hands-free:

**Voice command:** “Change material of the roof.”

```python
Gui.Selection.addSelection('Unnamed', 'Roof')
Gui.runCommand('BIM_Material', 0)
```

#### B. Hands-free material creation:

```python
material = Arch.makeMaterial()
material.Label = "Wood"
material.Material["Name"] = "Wood"
material.Material["Density"] = "600 kg/m^3"
material.Material["YoungsModulus"] = "10000 MPa"
roof = FreeCAD.ActiveDocument.getObject("Roof")
roof.Material = material
doc.recompute()
```

### 9. IFC Operations

#### A. Assigning IFC class

```python
FreeCAD.getDocument('Unnamed').getObject('Roof').IfcType = u"Roof"
FreeCAD.getDocument('Unnamed').getObject('Roof').PredefinedType = u"GABLE_ROOF"
```

#### B. Open IFC Properties Window

```python
Gui.runCommand('BIM_IfcProperties', 0)
```

### 10. Creating Section Views

#### A. Add Section Plane

```python
section = Arch.makeSectionPlane([FreeCAD.ActiveDocument.BuildingPart])
```

#### B. Move Section Plane

```python
FreeCAD.getDocument('Test_simple_house').getObject('BuildingPart').Placement = App.Placement(App.Vector(X, Y, Z), App.Rotation(App.Vector(0,0,1), 0))
```

#### C. Generate 2D Plan

```python
sv0 = Draft.make_shape2dview(FreeCAD.ActiveDocument.Section, FreeCAD.Vector(X, Y, Z))
```

---

Let me know if you want a downloadable `.md` file or to turn this into a PDF for submission/documentation.
