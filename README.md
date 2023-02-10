# LMS Annotations Extractor

[![Open in Streamlit][streamlit-badge]][tool]
[![Open in Colab][colab-badge]][extractor-notebook]
![Release Badge][github-release]

## Description

In this repository you can find the `Extractor Tool` used to generate the
annotation files for the **Leeds Multi-session Scripted Speech Corpus** (LMS) Project.

## Authors

- PI: Leendert Plug <l.plug@leeds.ac.uk>
- PDRA: James Carter <j.m.a.carter@leeds.ac.uk>
- RSE: Patricia Ternes <p.ternesdallagnollo@leeds.ac.uk>

## Instructions: Streamlit

1. **Open** the `LMS Annotation Extractor Tool` on Streamlit by clicking this button [![Open in Streamlit][streamlit-badge]][tool]
2. **Upload** the raw LMS/PsychoPy log file using the `Browse Files` button or `Drag\Drop` in grey box.
3. **Variables:** use the dropdown boxes to navigate and select the desired values, then click `Submit`.
4. **Outputs:** click `Download Output` to download the outputs.

## Instructions: Jupyter Notebook

1. Run the `extractor-notebook` on Google Colab by clicking this button [![Open in Colab][colab-badge]][extractor-notebook]
   - Note: you will need a Google account
2. Fill the talker/session values in the first code box (these values are used to properly name the output files):

```python
talker_ID = "01"
session_ID = "S1"
talker_gender = "F"
```

3. Execute all cells. You can do this by
   - click in (Runtime > Run All)
   - or via Keyboard Shortcut: `ctrl + F9`
     - *Note 1: A warning may be displayed. Click in `Run anyway`.*
     - *Note 2: Before running any cell you will be connected to a virtual machine. This may take a few seconds - Just wait.*
4. Once the program starts running, it will quickly stop at the second cell. At this moment you must click on the `Choose files` button to select the input file (recording csv log).
5. The following code cells should run automatically and will conclude with the automatic download of output files.
   - Depending on your web browser a box may appear asking if you want to download multiple files. Just click `Allow`.
6. If you have more than one file to extract information from it, just repeat steps 2, 3, 4 and 5
7. To finish you can:
   - click in (Runtime > Disconnect and Delete Runtime).

<!-- links -->
[colab-badge]: https://colab.research.google.com/assets/colab-badge.svg
[extractor-notebook]: https://colab.research.google.com/github/patricia-ternes/LMS_annotations_extractor/blob/main/extractor.ipynb
[streamlit-badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[tool]: https://patricia-ternes-lms-annotations-extractor.streamlit.app/
[github-release]: https://img.shields.io/github/v/release/patricia-ternes/LMS_annotations_extractor