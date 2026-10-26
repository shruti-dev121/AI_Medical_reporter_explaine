from django import forms


class ReportUploadForm(forms.Form):
    report = forms.FileField(
        label="Upload your medical report",
        help_text="Supported formats: PDF and TXT"
    )

    def clean_report(self):
        file = self.cleaned_data["report"]

        allowed_extensions = [".pdf", ".txt"]
        filename = file.name.lower()

        if not any(filename.endswith(ext) for ext in allowed_extensions):
            raise forms.ValidationError(
                "Please upload a PDF or TXT file."
            )

        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "File size must be less than 5 MB."
            )

        return file