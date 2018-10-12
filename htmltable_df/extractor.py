#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

from pyquery import PyQuery as pq, PyQuery
import pandas as pd
import os
import csv


class Extractor(object):
    def __init__(self, table, jquery='table', **kwargs):
        # input is PyQuery
        if isinstance(table, PyQuery):
            self._table = table(jquery)
        # input is str/unicode
        elif isinstance(table, str):
            self._table = pq(table)(jquery)
        else:
            raise Exception('unrecognized type')

        if 'transformer' in kwargs:
            self._transformer = kwargs['transformer']
        else:
            self._transformer = str

        self._output = []

        self.header = 0
        self.parse()

    def parse(self):
        self._output = []
        row_ind = 0
        col_ind = 0

        for row in self._table('tr').items():
            if row('th'):
                self.header += 1
            else:
                break
        if self.header == 0:
            self.header = 1

        for row in self._table('tr').items():
            # record the smallest row_span, so that we know how many rows
            # we should skip
            smallest_row_span = 1

            for cell in row('td,th').items():
                # check multiple rows
                # pdb.set_trace()
                row_span = int(cell.attr('rowspan')) if cell.attr('rowspan') else 1

                # try updating smallest_row_span
                smallest_row_span = min(smallest_row_span, row_span)

                # check multiple columns
                col_span = int(cell.attr('colspan')) if cell.attr('colspan') else 1

                # find the right index
                while True:
                    if self._check_cell_validity(row_ind, col_ind):
                        break
                    col_ind += 1

                # insert into self._output
                try:
                    self._insert(row_ind, col_ind, row_span, col_span, self._transformer(cell.text()))
                except UnicodeEncodeError:
                    raise Exception('Failed to decode text; you might want to specify kwargs transformer=unicode')

                # update col_ind
                col_ind += col_span

            # update row_ind
            row_ind += smallest_row_span
            col_ind = 0
        return self

    def return_list(self):
        return self._output

    def write_to_csv(self, path='.'):
        with open(os.path.join(path, 'output.csv'), 'w') as csv_file:
            table_writer = csv.writer(csv_file)
            for row in self._output:
                table_writer.writerow(row)
        return

    def df(self, header=None):
        if header:
            self.header = header
        data = self._output
        columns = [r[0] if len(set(r)) == 1 else re.sub('\s', '', '_'.join(r).strip('_')) for r in
                   list(zip(*data[:self.header]))]
        data = pd.DataFrame(data[self.header:], columns=columns)
        data = data.applymap(lambda x: x.strip().replace(',', ''))

        return data

    def _check_validity(self, i, j, height, width):
        """
        check if a rectangle (i, j, height, width) can be put into self.output
        """
        return all(self._check_cell_validity(ii, jj) for ii in range(i, i + height) for jj in range(j, j + width))

    def _check_cell_validity(self, i, j):
        """
        check if a cell (i, j) can be put into self._output
        """
        if i >= len(self._output):
            return True
        if j >= len(self._output[i]):
            return True
        if self._output[i][j] is None:
            return True
        return False

    def _insert(self, i, j, height, width, val):
        # pdb.set_trace()
        for ii in range(i, i + height):
            for jj in range(j, j + width):
                self._insert_cell(ii, jj, val)

    def _insert_cell(self, i, j, val):
        while i >= len(self._output):
            self._output.append([])
        while j >= len(self._output[i]):
            self._output[i].append(None)

        if self._output[i][j] is None:
            self._output[i][j] = val
