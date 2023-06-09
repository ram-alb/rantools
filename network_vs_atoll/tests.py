import os
from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from network_vs_atoll import views


def fake_main():
    """Fake main functions which returns compare results."""
    node1 = 'Almaty'
    node2 = 'Shymkent'
    node1_diff = [
        {
            'subnetwrok': node1,
            'site': 'nr_site1',
            'cell': 'nr_cell11',
            'parameter': 'pci',
            'network value': 100,
            'atoll value': 200,
        },
        {
            'subnetwrok': node1,
            'site': 'nr_site2',
            'cell': 'nr_cell21',
            'parameter': 'cellid',
            'network value': 2,
            'atoll value': 3,
        },
    ]
    node2_diff = [
        {
            'subnetwrok': node2,
            'site': 'nr_site3',
            'cell': 'nr_cell31',
            'parameter': 'pci',
            'network value': 22,
            'atoll value': 23,
        },
    ]

    nr_deltas = {
        node1: node1_diff,
        node2: node2_diff,
        'Total': node1_diff + node2_diff,
    }

    deltas = {
        'NR': nr_deltas,
    }

    deltas_by_nodes = [
        {'technology': 'NR', 'diffs': {node1: 2, node2: 1, 'Total': 3}},
    ]

    return (deltas, deltas_by_nodes)


class NetworkVsAtollViewTests(TestCase):
    """Tests for NetworkVsAtollView."""

    def setUp(self):
        """Test GET request."""
        self.client = Client()
        self.url = reverse('network_vs_atoll')
        views.main = fake_main

    def test_get(self):
        """Test GET request."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('diff', response.context)
        self.assertContains(response, '<td>NR</td>')
        self.assertContains(response, '<td>3</td>')
        self.assertContains(response, 'Almaty')
        self.assertContains(response, 'Shymkent')

    def test_post(self):
        """Test POST request."""
        response = self.client.post(
            self.url,
            {'technology': 'NR', 'node': 'Almaty'},
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response['Content-Type'],
            'application/vnd.ms-excel',
        )
        self.assertEqual(
            response['Content-Disposition'],
            'attachment; filename="Almaty.xlsx"',
        )
        file_path = 'network_vs_atoll/reports/Almaty.xlsx'
        if os.path.exists(file_path):
            os.remove(file_path)
