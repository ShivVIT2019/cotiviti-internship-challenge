import google.generativeai as genai
import time

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

print("=" * 60)
print("  COTIVITI AGENTIC AI - CLINICAL DECISION SUPPORT POC")
print("=" * 60)

patient = {
    "name": "John Martinez",
    "age": 67,
    "conditions": ["Type 2 Diabetes", "Hypertension", "CKD Stage 3"],
    "medications": ["Metformin 1000mg", "Lisinopril 10mg", "Atorvastatin 40mg"],
    "last_hba1c": "8.2%",
    "last_visit": "4 months ago",
    "insurance": "Medicare Advantage"
}

print(f"\nPATIENT: {patient['name']}, Age {patient['age']}")
print(f"Conditions: {', '.join(patient['conditions'])}")
print(f"Medications: {', '.join(patient['medications'])}")
print(f"Last HbA1c: {patient['last_hba1c']}")
print(f"Last Visit: {patient['last_visit']}")
print("\n" + "=" * 60)

print("\nAGENT 1: Care Gap Detection")
print("Analyzing patient record against HEDIS guidelines...")
time.sleep(1)
prompt1 = f"""
You are a clinical care gap detection agent for Cotiviti.
Analyze this patient and identify 2-3 care gaps based on HEDIS quality measures.
Patient: {patient}
Format as a numbered list. Be concise and clinical.
"""
response1 = model.generate_content(prompt1)
care_gaps = response1.text
print(care_gaps)

print("\nAGENT 2: Drug Interaction and Safety Check")
print("Checking medications for interactions and contraindications...")
time.sleep(1)
prompt2 = f"""
You are a clinical pharmacology agent.
Review this medication list for a patient with {', '.join(patient['conditions'])}.
Medications: {', '.join(patient['medications'])}
Check for drug interactions, contraindications given CKD Stage 3, and dosing concerns.
Format as a numbered list. Be concise and clinical.
"""
response2 = model.generate_content(prompt2)
drug_check = response2.text
print(drug_check)

print("\nAGENT 3: Clinical Decision Recommendation")
print("Synthesizing findings and generating recommendations...")
time.sleep(1)
prompt3 = f"""
You are a senior clinical decision support agent for Cotiviti.
Based on the following, generate recommendations for the care coordinator.

Patient: {patient['name']}, {patient['age']}yo with {', '.join(patient['conditions'])}
Care Gaps: {care_gaps}
Pharmacology Concerns: {drug_check}

Generate:
1. Top 3 priority actions for the care coordinator
2. Recommended next appointment timeline
3. Prior authorization flags if any

Be specific, actionable, and concise.
"""
response3 = model.generate_content(prompt3)
recommendation = response3.text
print(recommendation)

print("\n" + "=" * 60)
print("HUMAN-IN-THE-LOOP CHECKPOINT")
print("Care coordinator must review before any action is taken.")
print("=" * 60)
approval = input("\nApprove these recommendations? (yes/no): ").strip().lower()

if approval == "yes":
    print("\nApproved. Generating outreach task...")
    time.sleep(1)
    print(f"""
OUTREACH TASK CREATED:
Patient: {patient['name']}
Priority: HIGH
Action: Schedule follow-up within 30 days
Insurance: {patient['insurance']}
Status: Pending care coordinator contact
    """)
else:
    print("\nSent back for clinical review. No action taken.")

print("=" * 60)
print("  POC COMPLETE - Cotiviti Agentic AI Pipeline")
print("=" * 60)