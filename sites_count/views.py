from datetime import date

from django.contrib import messages
from django.shortcuts import render
from django.views import View

from sites_count.forms import SiteCountForm
from sites_count.src.main import get_site_data


class SitesCountView(View):
    """A view for displaying site counts."""

    template_path = 'sites_count/sites_count.html'
    year = 2023
    month = 5
    day = 15
    started_date = date(year, month, day)

    def get(self, request, *args, **kwargs):
        """Handle GET requests to the view and renders the site count form."""
        sites_data = get_site_data('operator')
        context = {
            'form': SiteCountForm(),
            'sites': sites_data,
            'header': 'Operator',
        }
        return render(request, self.template_path, context)

    def post(self, request, *args, **kwargs):
        """Handle POST requests to the view and processes the submitted form."""
        form = SiteCountForm(request.POST)
        if form.is_valid():
            requested_date = form.cleaned_data['date']

            if requested_date < self.started_date:
                messages.error(
                    request,
                    'No data before 15 May 2023',
                )
                return render(request, self.template_path, {'form': form})
            if requested_date > date.today():
                messages.error(
                    request,
                    'No data from the future :)',
                )
                return render(request, self.template_path, {'form': form})

            table_type = form.cleaned_data['table_type']
            sites_data = get_site_data(table_type, requested_date)
            header = table_type.capitalize()
            context = {'form': form, 'sites': sites_data, 'header': header}

            return render(request, self.template_path, context)

        return render(request, self.template_path, {'form': form})
