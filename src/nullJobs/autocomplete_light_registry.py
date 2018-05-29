import autocomplete_light as al
from jobApplications.models import *

al.register(JobPostingModel ,
    search_fields = ["^job_title"],
    attrs={
        "placeholder":"Category",
        "data-autocomplete-minimum-characters":1,
    },
    widget_attrs={
        "data-widget-maximum-values":4,
        "class":"modern-style",
    },
)
