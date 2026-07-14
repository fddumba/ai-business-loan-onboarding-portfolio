from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI(
    title="AI Loan Onboarding Integration Service",
    description="Prototype API service that maps AI extraction outputs to Camunda workflow variables.",
    version="0.1.0",
)


class ExtractionOutput(BaseModel):
    application_id: str
    document_readable: bool
    document_type: str
    company_name_extracted: str
    address_extracted: str
    document_date: str
    company_name_match: bool
    address_match: bool
    missing_or_unclear_fields: List[str]
    extraction_summary: str
    workflow_signal: str


SIGNAL_TO_ROUTE = {
    "EVIDENCE_MATCHED": "CLEAN_CASE",
    "DOCUMENT_EXPIRED_OR_WEAK": "REQUEST_NEW_DOCUMENT",
    "MISMATCH_REQUIRES_REVIEW": "HUMAN_REVIEW",
    "REGISTRY_REQUIRES_INVESTIGATION": "MANUAL_INVESTIGATION",
}


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "AI Loan Onboarding Integration Service"
    }


@app.post("/map-to-camunda-variables")
def map_to_camunda_variables(extraction: ExtractionOutput):
    verification_route = SIGNAL_TO_ROUTE.get(extraction.workflow_signal)

    if verification_route is None:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported workflow_signal: {extraction.workflow_signal}"
        )

    return {
        "applicationId": extraction.application_id,
        "documentReadable": extraction.document_readable,
        "documentType": extraction.document_type,
        "extractedCompanyName": extraction.company_name_extracted,
        "extractedAddress": extraction.address_extracted,
        "documentDate": extraction.document_date,
        "companyNameMatch": extraction.company_name_match,
        "addressMatch": extraction.address_match,
        "missingOrUnclearFields": extraction.missing_or_unclear_fields,
        "aiExtractionSummary": extraction.extraction_summary,
        "workflowSignal": extraction.workflow_signal,
        "verificationRoute": verification_route,
    }