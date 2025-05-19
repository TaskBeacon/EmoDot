from psyflow import StimUnit
import os
from functools import partial
from src import assign_stim_from_condition

def run_trial(win, kb, settings, condition, stim_bank, asset_pool, trigger_sender):
    """
    Run a single emotional dot-target trial:
    fixation → face pair → target + response
    """
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, triggersender=trigger_sender)

    trial_info = assign_stim_from_condition(condition, asset_pool)
    left_stim = stim_bank.rebuild('left_stim', image=os.path.join('assets', trial_info['left_stim']))
    right_stim = stim_bank.rebuild('right_stim', image=os.path.join('assets', trial_info['right_stim']))


    # --- Fixation ---
    make_unit(unit_label='fixation').add_stim(stim_bank.get("fixation")) \
        .show(duration=settings.fixation_duration, onset_trigger=settings.triggers.get("fixation_onset")) \
        .to_dict(trial_data)

    # --- Cue Pair ---
   
    make_unit(unit_label='cues').add_stim(left_stim).add_stim(right_stim) \
        .show(duration=settings.cue_duration, onset_trigger=settings.triggers.get(f"{condition}_cue_onset")) \
        .to_dict(trial_data)

    # interval
    make_unit(unit_label='itnerval').add_stim(stim_bank.get("fixation")) \
        .show(duration=settings.interval_duration)
    # --- target + Response ---
    target_stim = stim_bank.get(f"{trial_info['target_position']}_target")
    target_unit = make_unit(unit_label="target").add_stim(target_stim)
    correct_key = settings.left_key if trial_info['target_position'] == 'left' else settings.right_key
    target_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_key,
        duration=settings.target_duration,
        onset_trigger=settings.triggers.get(f"{condition}_target_onset"),
        response_trigger=settings.triggers.get("key_press"),
        timeout_trigger=settings.triggers.get("no_response"),
        terminate_on_response=True
    )
    target_unit.to_dict(trial_data)


    return trial_data