from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.autotag_pdf_operation import AutotagPDFOperation
from adobe.pdfservices.operation.internal.api.dto.request.autotagpdf.autotag_pdf_output import AutotagPDFOutput
from adobe.pdfservices.operation.pdfops.options.autotagpdf.autotag_pdf_options import AutotagPDFOptions

import logging
import os.path
from pathlib import Path


input_pdf = "./input/Title-and-Images-not-tagged.pdf"

output_path = "./output/AutotagPDF/"

Path(output_path).mkdir(parents=True, exist_ok=True)
tagged_pdf_path = f'{output_path}{input_pdf}-tagged.pdf'
report_path = f'{output_path}{input_pdf}-report.xlsx'

try:
    # Initial setup, create credentials instance.
    credentials = Credentials.service_principal_credentials_builder() \
        .with_client_id("") \
        .with_client_secret("") \
        .build()

    # Create an ExecutionContext using credentials and create a new operation instance.
    execution_context = ExecutionContext.create(credentials)
    autotag_pdf_operation = AutotagPDFOperation.create_new()

    # Set operation input from a source file.
    source = FileRef.create_from_local_file(input_pdf)
    autotag_pdf_operation.set_input(source)

    # Build AutotagPDF options and set them into the operation
    autotag_pdf_options: AutotagPDFOptions = AutotagPDFOptions.builder() \
        .with_generate_report() \
        .build()
    autotag_pdf_operation.set_options(autotag_pdf_options)

    # Execute the operation.
    autotag_pdf_output: AutotagPDFOutput = autotag_pdf_operation.execute(execution_context)

    # Save the result to the specified location.
    autotag_pdf_output.get_tagged_pdf().save_as(tagged_pdf_path)
    autotag_pdf_output.get_report().save_as(report_path)

    print("Successfully tagged information in PDF.")

except (ServiceApiException, ServiceUsageException, SdkException) as e:
    logging.exception(f"Exception encountered while executing operation : {e}")
