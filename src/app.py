import streamlit as st
import pandas as pd
from zipfile import ZipFile
import os

# Project: Leeds Multi-session Scripted Speech (LMS)
# Tool: LSM Annotations Extractor Tool
# Description: Tool to extract/organise files from the raw LMS/PsychoPy log file
# Outputs: 6 annotation text files; 1 segmentation text file; 1 tapping csv file
# Code Author: Patricia Ternes <p.ternesdallagnollo@leeds.ac.uk>
# GitHub: https://github.com/patricia-ternes/LMS_annotations_extractor
# Streamlit deployed: https://patricia-ternes-lms-annotations-extractor.streamlit.app/


def main():
    st.title("LMS Annotation Extractor Tool")
    st.markdown(
        "This app extracts/organises files from the raw LMS/PsychoPy log file. &nbsp;"
        "[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/patricia-ternes/LMS_annotations_extractor)"
    )
    st.markdown("***")

    st.subheader("Dataset")
    data_file = st.file_uploader("Upload the input CSV file", type=["csv"])
    columns = ["task_name", "item_text", "trial_tapping_button.timesOn"]
    if data_file:
        data = pd.read_csv(data_file, usecols=columns)

    corpus = "LMS"
    tasks_ID = ["SYL", "WOR", "PAS", "SNO", "SFA", "SCL"]
    task_names = [
        "pa",
        "word",
        "passage",
        "sentence_normal",
        "sentence_fast",
        "sentence_clear",
    ]
    participants_ID = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
    ]
    participants_Gender = ["F", "M", "N"]
    sessions_ID = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]

    if data_file:
        st.subheader("Variables")
        st.markdown(
            "Select the desired variable values, then click the 'Submit' button"
        )
        with st.form("variables_form"):

            # Add select boxes side by side:
            col1, col2, col3 = st.columns(3)
            with col1:
                talker_ID = st.selectbox(
                    "Participant ID:", participants_ID, label_visibility="visible"
                )
            with col2:
                talker_G = st.selectbox(
                    "Participant Gender:",
                    participants_Gender,
                    label_visibility="visible",
                )
            with col3:
                session_ID = st.selectbox(
                    "session ID:", sessions_ID, label_visibility="visible"
                )

            # Add Submit Button
            submitted = st.form_submit_button("Submit")

        if submitted:
            # Repeat the following for every task
            output_path = "_".join([corpus, talker_ID, talker_G, session_ID])
            outputs, names = [], []
            segmentation = ""
            for i in range(len(tasks_ID)):
                task_df = data[
                    data["task_name"] == task_names[i]
                ]  # selects rows according to the task
                task_df = task_df[
                    "item_text"
                ].dropna()  # drop empty rows (first row for every task)
                task_df.index = (
                    task_df.reset_index(drop=True).index + 1
                )  # reset index, starting at 1
                segmentation += (
                    "\t".join(task_df) + "\n\n"
                )  # organise text to segmentation file
                task_df = (
                    task_df.index.astype(str) + ". " + task_df
                )  # add index to text

                # Define output name, based in variables
                output_name = "_".join(
                    [corpus, tasks_ID[i], talker_ID, talker_G, session_ID + ".txt"]
                )

                # Store data and names
                outputs.append(task_df)
                names.append(output_name)

            # Tapping extraction
            tapping_df = data[
                data["task_name"] == "tapping"
            ]  # select rows with tapping values
            tapping_df = (
                tapping_df["trial_tapping_button.timesOn"]
                .dropna()
                .reset_index(drop=True)
            )  # remove empty row
            tapping_str = "".join(tapping_df)  # transform the cell into a string
            tapping_str = tapping_str.replace("[", "")  # remove character
            tapping_str = tapping_str.replace("]", "")  # remove character
            tapping = "\n".join(tapping_str.split(", "))

            # Transform data into a zip file
            with ZipFile("output.zip", "w") as csv_zip:
                # annotation files
                for i in range(len(outputs)):
                    csv_zip.writestr(names[i], "\n".join(outputs[i]))

                # segmentation file
                csv_zip.writestr(output_path + "_segmentation.txt", segmentation)

                # tapping file
                csv_zip.writestr(output_path + "_tapping.csv", tapping)

            # Download Zip File
            st.subheader("Outputs")
            with open("output.zip", "rb") as file:
                st.download_button(
                    label="Download Output", data=file, file_name=output_path + ".zip"
                )

        st.markdown("***")
        st.subheader("Clean Data")
        if st.button("Clean Data"):
            del data_file, data
            os.remove("output.zip")


if __name__ == "__main__":
    main()
