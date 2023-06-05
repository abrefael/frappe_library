// Copyright (c) 2023, me and contributors
// For license information, please see license.txt

frappe.ui.form.on('Books and Articles', {
	guess(frm) {
	    var doi = frm.doc.doi;
		var isbn = frm.doc.isbn;
		var file = frm.doc.pdf_file;
		frm.call('guess_pdf_data',{'filepath': file,'doi': doi,'isbn': isbn})
			.then(r => {
				var xx = r.message;
				if (xx == "null") {
					return;
				}
				else {
					var title = xx.title;
					var publisher = xx.publisher;
					isbn = xx.isbn;
					doi = xx.doi;
					var year = xx.year;
					var month = xx.month;
					var type = xx.type;
					var authors = xx.authors;
					if (title){
						frm.set_value('title',title);
					}
					if (type){
						frm.set_value('type',type);
					}
					if (year){
						frm.set_value('year',year);
					}
					if (month){
						frm.set_value('month',month);
					}
					if (isbn){
						frm.set_value('isbn',isbn);
					}
					if (doi){
						frm.set_value('doi',doi);
					}
					if (publisher){
						frm.set_value('publisher',publisher);
					}
					if (authors){
						var author_child_table = frm.doc.authors;
						var row;
						for (let i = 0; i < authors.length; i++) {
							row = frm.add_child("authors");
							given = author_child_table[i].given;
							if(authors[i].family){
								row.family = authors[i].family;
							}
							refresh_field("authors");
						}
					}
					
					
				}
			});
	}
});