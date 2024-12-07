# Idea: create a script which can send a selection of assets from unreal engine to blender and possibly create a material aswell.
# Get model out of unreal. Json? Yaml? also export the FBX. or use the source one?
# Have blender read that information. and import the assets

# Select assets in unreal -> 
# run python script which gets selects assets and exports them to temp file -> 
# gets currently open blender or opens it. could possibly open a headless blender to set the scene up then open that saved scene. _>
# imports da meshes

import unreal
import json

sel = unreal.EditorActorSubsystem.get_selected_level_actors(unreal.get_editor_subsystem(unreal.EditorActorSubsystem))
data = {}
for actor in sel:
    print(f'actor: {actor.get_name()}, loc: {actor.get_actor_location()}')
    if not isinstance(actor, unreal.StaticMeshActor):
        continue
    mesh_component = actor.static_mesh_component
    if not mesh_component:
        print(f'{actor.get_name()} has no mesh component')
        continue
    mesh = mesh_component.static_mesh
    if not mesh:
        print(f'{actor.get_name()} has no satic mesh.')
        continue
    import_data = mesh.get_editor_property('asset_import_data')
    if not import_data:
        print(f'{actor.get_name()} has no import data')
        continue
    import_data = import_data.get_first_filename()
    loc = [actor.get_actor_location().x, actor.get_actor_location().y, actor.get_actor_location().z]
    rot = [actor.get_actor_rotation().roll, actor.get_actor_rotation().pitch, actor.get_actor_rotation().yaw]
    scale = [actor.get_actor_scale3d().x, actor.get_actor_scale3d().y, actor.get_actor_scale3d().z]
    data.update({actor.get_name(): {'transform': {'loc': loc, 'rot': rot, 'scale': scale}, 'source_mesh': import_data}})
with open(r'C:\Git\CodeProjects\CodeProjects\blender\data.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True)

with open(r'C:\Git\CodeProjects\CodeProjects\blender\data.json', 'r') as file:
    data = json.load(file)
    print(data)