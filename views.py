# submit exam answers
def submit(request):
    if request.method == "POST":
        return render(request, "submit.html")
    return render(request, "submit.html")


# show exam result
def show_exam_result(request):
    result = "Exam result will appear here"
    return render(request, "result.html", {"result": result})