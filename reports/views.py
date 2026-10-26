
from django.shortcuts import render
from .forms import ReportUploadForm
from .services import extract_text, explain_report
from openai import OpenAIError
from django.shortcuts import render
from .forms import ReportUploadForm
from .services import extract_text, explain_report
from .models import ReportAnalysis



def upload_report(request):
    extracted_text = None
    explanation = None
    error = None

    if request.method == "POST":
        form = ReportUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data["report"]

            try:
                extracted_text = extract_text(uploaded_file)
                explanation = explain_report(extracted_text)

                ReportAnalysis.objects.create(
                filename=uploaded_file.name,
                explanation=explanation
)

            except ValueError as e:
                error = str(e)

            except OpenAIError as e:
                print("OpenAI ERROR:", repr(e))
                error = (
                    "AI request failed. Check your API key, "
                    "model access, billing, and internet connection."
                )

            except Exception as e:
                print("GENERAL ERROR:", repr(e))
                error = f"Unexpected error: {e}"

    else:
        form = ReportUploadForm()

    return render(request, "reports/upload.html", {
        "form": form,
        "extracted_text": extracted_text,
        "explanation": explanation,
        "error": error,
    })

def report_history(request):
    reports = ReportAnalysis.objects.order_by("-created_at")

    return render(
        request,
        "reports/history.html",
        {"reports": reports}
    )
