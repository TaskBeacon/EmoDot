# Emotional Dot-Probe Task – PsyFlow Version

This task implements an emotional dot-probe paradigm to measure attentional bias towards emotional versus neutral stimuli. Participants respond to the location of a target dot that appears after the brief presentation of two face stimuli. The task is built using the [PsyFlow](https://taskbeacon.github.io/psyflow/) framework.

---

## Task Overview

Participants first view a fixation cross, followed by a brief presentation of a pair of face images (e.g., positive vs. neutral, negative vs. neutral). After a short interval, a small target dot appears on either the left or right side. Participants must quickly indicate the location of the dot by pressing the left or right arrow key.

This task assesses attentional biases toward emotional stimuli and is widely used in studies of anxiety, depression, and emotional regulation.

---

## Task Flow

| Step        | Description |
|-|-|
| Instruction | A textbox (`instruction_text`) presents task instructions in Chinese. Participant presses the **space bar** to start. |
| Fixation    | A fixation cross "+" is shown at the center of the screen. |
| Cue Pair    | A pair of face images (left and right) are displayed briefly. |
| Interval    | A short blank screen or fixation is shown after the faces. |
| Target      | A dot appears either on the left or right side; participant responds via arrow keys. |
| Block Break | After each block, performance feedback is presented and participants rest. |
| Goodbye     | A final thank-you screen ends the session.

---

## Configuration Summary

All key settings are stored in the `config/config.yaml` file.

### Subject Info (`subinfo_fields`)
Participants are registered with:
- **Subject ID** (3-digit number from 101–999)
- **Session Name**
- **Experimenter Name**
- **Gender** (Male or Female)

Localized prompts are available via `subinfo_mapping`.

---

### Window Settings (`window`)
- Resolution: `1920 × 1080`
- Units: `deg`
- Fullscreen: `True`
- Monitor: `testMonitor`
- Background color: `black`

---

### Stimuli (`stimuli`)
| Stimulus Name       | Type    | Description |
|-|-|-|
| `fixation`          | `text`  | Central fixation cross "+" |
| `left_stim`, `right_stim` | `image` | Face stimuli dynamically assigned per trial |
| `left_target`, `right_target` | `circle` | Target dots shown left or right |
| `block_break`       | `text`  | Mid-task break message |
| `instruction_text`  | `textbox` | Task instructions in Chinese |
| `good_bye`          | `textbox` | End-of-task thank-you screen |

Stimulus images are dynamically assigned based on trial conditions using an `asset_pool`.

---

### Timing (`timing`)
| Phase                | Duration |
|-|-|
| Fixation             | 0.3 seconds |
| Face Cue             | 0.5 seconds |
| Interval             | 0.4–0.6 seconds (randomized) |
| Target Response Time | 1.2 seconds |

---

### Conditions (`task.conditions`)
Each condition represents the combination of:
- Emotion pair (Positive-Neutral, Negative-Neutral, Neutral-Neutral)
- Gender of faces (Female, Male)
- Target side (Left, Right)

Example condition codes:
- `PN_F_L` – Positive (left) / Neutral (right), Female faces, Target Left
- `SN_M_R` – Negative (left) / Neutral (right), Male faces, Target Right
- etc.

There are 18 conditions in total.

---

### Triggers (`triggers`)
Each condition has a full set of triggers:

| Event         | Trigger Code Example (for `PN_F_L`) |
|-|-|
| Fixation Onset | 11 |
| Cue Onset      | 12 |
| Target Onset   | 13 |
| Key Press      | 14 |
| No Response    | 15 |

General experiment and block onset/end triggers:
- **Experiment Start**: 98
- **Experiment End**: 99
- **Block Start**: 198
- **Block End**: 199

---

## Running the Task
```python
python main.py
```
