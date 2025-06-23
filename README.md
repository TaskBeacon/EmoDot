# Emotional Dot-Probe Task (EmoDot)

| Field                | Value                        |
|----------------------|------------------------------|
| Name                 | Emotional Dot-Probe Task (EmoDot) |
| Version              | main (1.0)                          |
| URL / Repository     | https://github.com/TaskBeacon/EmoDot   |
| Short Description    | A task for assessing attentional bias toward emotional facial stimuli |
| Created By           | Zhipeng Cao (zhipeng30@foxmail.com)          |
| Date Updated         | 2025/06/22      |
| PsyFlow Version      | 0.1.0               |
| PsychoPy Version     | 2025.1.1                        |
| Modality             | Behavior/EEG                      |

```{note}
The emotional expression stimulus are not publicly available due to potential copyright issues.
```


## 1. Task Overview

The Emotional Dot-Probe (EmoDot) task assesses attentional biases toward emotional stimuli. Participants are briefly shown a pair of face images—one emotional (positive or negative) and one neutral—followed by a target (a white circle) appearing on the left or right side. Participants must quickly respond to the target’s position by pressing a corresponding key. The emotional valence, facial gender, and target location are all experimentally manipulated. The task also incorporates trial-by-trial stimulus randomization from a categorized image pool to ensure balanced and unpredictable face pairings.

## 2. Task Flow

### Block-Level Flow

| Step                       | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Load Config                | Load task configuration, subject info schema, stimuli, triggers             |
| Collect Subject Info       | Capture ID, name, age, gender                                               |
| Setup Triggers             | Initialize trigger sender via serial port                                   |
| Initialize Window/Input    | Set up PsychoPy window and keyboard                                         |
| Load Stimuli               | Build static stimuli (shapes, text, etc.), preload and convert instructions |
| Load Assets                | Retrieve image files from asset folder and organize by category             |
| Initialize Stim Pool       | Create randomized per-category pools for sampling stimuli                  |
| Show Instructions          | Display instruction text and synthesized voice                              |
| Loop Over Blocks           | Run 3 blocks × 60 trials (with stimulus pairing + response logging)         |
| Show Block Feedback        | Display summary (accuracy) after each block                                 |
| Show Goodbye               | Display thank-you message                                                   |
| Save Data                  | Save full trial data to CSV                                                 |
| Close                      | Close serial connection and PsychoPy window                                 |

### Trial-Level Flow

| Step                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Fixation            | Present fixation cross (0.8–1.0s) with trigger                              |
| Cue Display         | Show pair of face images (left/right) for 0.5s with trigger                 |
| Interval            | Brief fixation interval (0.4–0.6s)                                          |
| Target              | Show white circle target on left or right; collect response (up to 1.0s)    |
| Response Logging    | Record accuracy, RT, and target location                                    |

### Other Logic

| Component                     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `AssetPool`                   | A class that manages condition-specific stimulus pools using shuffle-on-depletion logic |
| `get_stim_list_from_assets()` | Scans the `assets/` directory for `.bmp` images and categorizes them by prefix (e.g., HF, SAF) |
| `assign_stim_from_condition()`| Given a trial condition string (e.g., `PN_F_L`), selects appropriate stimuli and target side |
| Condition Encoding            | Each condition encodes emotion pairing (PN, SN, etc.), gender (M/F), and target side (L/R) |

These logic components collectively ensure:
- Dynamic, trial-specific face assignment per condition
- Balanced sampling across categories
- Prevention of stimulus repetition until category depletion
- Flexible extensibility for new emotion/gender pairings

## 3. Configuration Summary

### a. Subject Info

| Field       | Meaning                        |
|-------------|--------------------------------|
| subject_id  | Participant ID (101–999)       |
| subname     | Participant name (pinyin)      |
| age         | Age (5–60)                     |
| gender      | Gender (Male/Female)           |

### b. Window Settings

| Parameter             | Value         |
|-----------------------|---------------|
| size                  | [1920, 1080]  |
| units                 | deg           |
| screen                | 1             |
| bg_color              | black         |
| fullscreen            | True          |
| monitor_width_cm      | 59.7          |
| monitor_distance_cm   | 72            |

### c. Stimuli

| Name            | Type    | Description                                         |
|------------------|---------|-----------------------------------------------------|
| fixation         | text    | White "+" central fixation                          |
| left_stim        | image   | Face image on the left (dynamic)                    |
| right_stim       | image   | Face image on the right (dynamic)                   |
| left_target      | circle  | White circle target (left side)                     |
| right_target     | circle  | White circle target (right side)                    |
| block_break      | text    | Summary screen with accuracy between blocks         |
| instruction_text | textbox | Multi-line instructions on cue-target mapping       |
| good_bye         | textbox | Final message post-task                             |

### d. Timing

| Phase              | Duration (s)     |
|--------------------|------------------|
| fixation           | random 0.8–1.0   |
| cue display        | 0.5              |
| interval           | random 0.4–0.6   |
| target             | 1.0              |

### e. Triggers

| Event Type             | Example Code |
|------------------------|--------------|
| Task Start             | 98           |
| Task End               | 99           |
| Block Start/End        | 198 / 199    |
| Fixation Onset         | 11–201       |
| Cue Onset              | 12–202       |
| Target Onset           | 13–203       |
| Key Press              | 68           |
| No Response            | 69           |

*Note: Each condition (e.g., PN_F_L) has unique fixation/cue/target onset and response triggers.*

## 4. Methods (for academic publication)

Participants performed a computerized emotional dot-probe task designed to probe attentional biases toward emotional facial expressions. Each trial began with a fixation cross (0.8–1.0 seconds), followed by a pair of face stimuli (one emotional—positive or negative—and one neutral), presented side by side for 0.5 seconds. After a brief inter-stimulus interval (0.4–0.6 seconds), a target dot appeared on either the left or right side of the screen. Participants were instructed to respond as quickly and accurately as possible by pressing the “F” key for left and “J” for right.

The experimental conditions conterbalanced the emotional content (positive, negative, or neutral), the gender of the faces (male/female), and the target location (left/right). A pool of facial images was pre-organized by emotion and gender categories and dynamically sampled to prevent stimulus repetition. Each image pair was randomly drawn per trial while satisfying the specified emotion/gender constraints.

The experiment consisted of **3 blocks** with **60 trials each**, totaling **180 trials**. Trial types were fully randomized using a blocked condition design. At the end of each block, participants received feedback about their hit rate (i.e., correct target detections). 

## 5. References
>MacLeod, C., Mathews, A., & Tata, P. (1986). Attentional bias in emotional disorders. Journal of Abnormal Psychology, 95, 15–20.

>Van Rooijen, R., Ploeger, A., & Kret, M. E. (2017). The dot-probe task to measure emotional attention: A suitable measure in comparative studies?. Psychonomic bulletin & review, 24, 1686-1717.

A study that seems worth paying attention to

>Xu, I., Passell, E., Strong, R. W., Grinspoon, E., Jung, L., Wilmer, J. B., & Germine, L. T. (2025). No evidence of reliability across 36 variations of the emotional dot-probe task in 9,600 participants. Clinical Psychological Science, 13(2), 261-277.