import bpy
from . import cleanup_transform

cleanup_transform.register()
cleanup_transform.cleanup_and_transform()