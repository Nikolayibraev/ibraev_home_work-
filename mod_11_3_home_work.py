def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]



    try:
        module_name = obj.__module__
    except AttributeError:
        module_name = 'N/A'  # Если атрибут отсутствует, указываем 'N/A'

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name,
    }


    if isinstance(obj, (list, dict, set)):
        info['length'] = len(obj)

    return info





class SampleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"



sample_object = SampleClass("Alice")

object_info = introspection_info(sample_object)
print(object_info)

number_info = introspection_info(42)
print(number_info)