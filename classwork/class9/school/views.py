from django.shortcuts import render, redirect


results = {
    "John": "Passed with A grade",
    "Alice": "Passed with B grade",
    "Bob": "Failed",
}


def home(request):
    return redirect("results_page")


def results_page(request):
    return render(request, "results.html", {
        "title": "All Results",
        "results": results
    })


def view_result(request, student_name):
    result = results.get(student_name, "Result not found")
    return render(request, "result.html", {
        "title": "Result",
        "student_name": student_name,
        "result": result
    })
