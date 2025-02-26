import obspython as obs
import os

file_path = ""
interval = 1000
source_name = ""
previous_content = ""

# ------------------------------------------------------------

def update_text():
    global file_path
    global source_name
    global previous_content

    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        try:
            with open(file_path, 'r') as file:
                text = file.read()

                # Only update the source if the content has changed
                if previous_content != text:
                    settings = obs.obs_data_create()
                    obs.obs_data_set_string(settings, "text", text)
                    obs.obs_source_update(source, settings)
                    obs.obs_data_release(settings)

                    # Update the previous content
                    previous_content = text

        except FileNotFoundError:
            obs.script_log(obs.LOG_WARNING, f"File not found at path: {file_path}")

        obs.obs_source_release(source)

def refresh_pressed(props, prop):
    update_text()

# ------------------------------------------------------------

def script_description():
    return "Updates a text source with text retrieved from a text file at specified intervals."

def script_update(settings):
    global file_path
    global interval
    global source_name

    file_path = obs.obs_data_get_string(settings, "file_path")
    interval = obs.obs_data_get_int(settings, "interval")
    source_name = obs.obs_data_get_string(settings, "source")

    if file_path != "" and source_name != "":
        obs.timer_add(update_text, interval)

def script_defaults(settings):
    obs.obs_data_set_default_int(settings, "interval", 1000)

def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_text(props, "file_path", "File Path", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_int(props, "interval", "Update Interval (Milliseconds)", 1, 3600, 1)

    p = obs.obs_properties_add_list(props, "source", "Text Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)
            if source_id in ["text_gdiplus", "text_ft2_source"]:
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(p, name, name)

        obs.source_list_release(sources)

    obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
    return props