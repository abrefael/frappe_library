# Copyright (c) 2023, me and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BooksandArticles(Document):
	@frappe.whitelist()
	def guess_pdf_data(pdf_file_path = None, doi = None, isbn = None):
		import pdf2doi
		import isbnlib
		def guess (results, type = None):
			import json
			if type == 'doi' or type == 'DOI':
				return guess_with_doi(results)
			elif type == 'isbn' or type == 'ISBN':
				return guess_with_isbn(results)
			else:
				msg = '''Cannot identify the document.
					Please make sure file was OCRed.
				'''
				frappe.msgprint(msg=msg, title='Error')
				return "null"
		def guess_with_doi(results):
			import json
			json_object = json.loads(results)
			response = {}
			try:
				response['isbn'] = json_object['isbn-type'][0]['value']
			except:
				pass
			try:
				response['year'] = json_object['published-print']['date-parts'][0][0]
			except:
				pass
			try:
				response['month'] = json_object['published-print']['date-parts'][0][1]
			except:
				pass
			try:
				response['title'] = json_object['title']
			except:
				pass
			try:
				response['type'] = json_object['type']
			except:
				pass
			try:
				response['publisher'] = json_object['publisher']
			except:
				pass
			try:
				response['authors'] = json_object['authors'] #foreach author in authors{given = author.given, last = author.family}
			except:
				pass
			return(response)
		def guess_with_isbn(results):
			import json
			json_object = json.loads(results)
			response = {}
			try:
				response['title'] = json_object['Title']
			except:
				pass
			try:
				response['authors'] = json_object['Authors']
			except:
				pass
			try:
				response['publisher'] = json_object['Publisher']
			except:
				pass
			try:
				response['year'] = json_object['Year']
			except:
				pass
			return (response)
		msg = '''Cannot identify the document.
		Please make sure file was OCRed.
		'''
		if isbn:
			results, type = pdf2doi.validate(isbn,'isbn'), 'ISBN'
		elif doi:
			results, type = pdf2doi.validate(doi,'doi'), 'DOI'
		else:
			try:
				data = pdf2doi.pdf2doi(pdf_file_path)
				results, type = data['validation_info'], data['identifier_type']
			except:
				frappe.msgprint(msg=msg, title='Error')
				return "null"
		if not results:
				frappe.msgprint(msg=msg, title='Error')
				return "null"
		else:
			sending_data = guess (results, type)
			return sending_data