#!/usr/bin/python

"""
	Realizar una calculadora de las cuatro operaciones aritmeticas basicas
	(suma, resta, multiplicacion y division), siguiendo los principios REST,
	a la manera del sumador simple version REST.

	Daniel Crespo Beltran
	creespow
"""

import webapp
import socket

def analyze (operations):
	try:
		if len(operations.split("+")) == 2:
			return (int(operations.split("+")[0]) +
					int(operations.split("+")[1]))
		elif len(operations.split("-")) == 2:
			return (int(operations.split("-")[0]) -
					int(operations.split("-")[1]))
		elif len(operations.split("*")) == 2:
			return (int(operations.split("*")[0]) *
					int(operations.split("*")[1]))
		elif len(operations.split("/")) == 2:
			return (int(operations.split("/")[0]) /
					int(operations.split("/")[1]))
		else:
				return "Error de operacion"
	except ValueError:
			return "Value Error"



class calculadorarest(webapp.webApp):
	def parse (self, request):
		operations = request.split()[-1]
		httpmethod = request.split()[0]
		return (httpmethod, operations)

	def process (self, parsedRequest):
		(httpmethod, operations) = parsedRequest

		if httpmethod == "PUT":
			self.operacion = operations;
			return ("200 OK", "<html><body>La operacion es: "
					+ str(operations) + "</body></html>")
		elif httpmethod == "GET":
			try:
				result = analyze(self.operacion)
				return ("200 OK", "<html><body>El resultado es: "
						+ str(result) + "</body></html>")
			except AttributeError:
				return ("400 Not Found",
						"<html><body>Attribute Error</body></html>")


if __name__ == '__main__':
	serv = calculadorarest(socket.gethostname(), 1234)