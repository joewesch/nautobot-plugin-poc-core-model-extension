"""Filter extensions for poc_core_model_extension plugin."""
from django import forms

from nautobot.apps.filters import FilterExtension, MultiValueCharFilter
from nautobot.utilities.forms import DynamicModelChoiceField

from poc_core_model_extension.models import MyModel


class DeviceFilterExtension(FilterExtension):
    """Adding filters to JobResult."""

    model = "dcim.device"

    filterset_fields = {
        "poc_core_model_extension_mymodel": MultiValueCharFilter(field_name="mymodel__name"),
    }

    filterform_fields = {
        "poc_core_model_extension_mymodel__ic": DynamicModelChoiceField(
            queryset=MyModel.objects.all(),
            required=False,
            to_field_name="name",
            label="MyModel Search",
        ),
    }


filter_extensions = [DeviceFilterExtension]
