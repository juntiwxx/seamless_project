import pandas as pd

from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from .models import StudentInfo
from .forms import UploadFileForm

class UploadFileAdmin(admin.ModelAdmin):
    change_list_template = "admin/upload_file_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload/', self.admin_site.admin_view(self.upload_file_view), name='upload-file'),
        ]
        return custom_urls + urls

    def upload_file_view(self, request):
        data = None
        error_message = None

        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = request.FILES['file']

                if uploaded_file.name.endswith(('.xlsx', '.xls')):
                    df = pd.read_excel(uploaded_file)

                    if not df.empty:
                        df = pd.DataFrame(
                            df,
                            columns=['ACADEMIC_YEAR']
                        )

                        data = df.to_dict(orient='records')
                        request.session['data'] = data  # Store data in session for CSV download

                else:
                    error_message = "Invalid file format. Please upload an Excel file."
        else:
            form = UploadFileForm()

        context = dict(
            self.admin_site.each_context(request),
            form=form,
            data=data,
            error_message=error_message,
        )
        return TemplateResponse(request, "admin/upload_file.html", context)


admin.site.register(StudentInfo, UploadFileAdmin)