from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from network_vs_atoll.src.excel import fill_excel
from network_vs_atoll.src.main import main


class NetworkVsAtollView(View):
    """A view for displaying Network vs Atoll data."""

    diff = {}

    def get(self, request, *args, **kwargs):
        """Handle GET request to display diffs between Network and Atoll."""
        context = {}
        deltas, diff = main()
        context['diff'] = diff

        for tech, delta in deltas.items():
            self.diff[tech] = delta

        return render(request, 'network_vs_atoll/nva_index.html', context)

    def post(self, request, *args, **kwargs):
        """Handle POST request to fille report and send it for download."""
        technology = request.POST.get('technology')
        node = request.POST.get('node')

        report_path = fill_excel(node, self.diff[technology][node])
        with open(report_path, 'rb') as attachment:
            file_data = attachment.read()
            response = HttpResponse(
                file_data,
                content_type='application/vnd.ms-excel',
            )
            response['Content-Disposition'] = (
                f'attachment; filename="{node}.xlsx"'
            )
            return response
