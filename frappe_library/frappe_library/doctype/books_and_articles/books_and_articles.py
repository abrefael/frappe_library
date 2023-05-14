# Copyright (c) 2023, me and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BooksandArticles(Document):
	@frappe.whitelist()
	def guess_pdf_data(pdf_file_path = None, doi = None, isbn = None):
		import requests
		return 'Something'

