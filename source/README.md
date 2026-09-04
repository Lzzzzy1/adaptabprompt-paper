# Reproduction source

This directory is the portable source bundle for the archived AdapTabPrompt ICCEIC 2026 manuscript.

## Evidence contract

`work/paper_data.py` validates the immutable evidence snapshot in `evidence/` before exposing any number to the manuscript generator. The snapshot is fixed by these SHA-256 digests:

- `report.json`: `C317A76CA24B620FD5ADD0E024A5090385AEE7216AD83666BE733668911010FC`
- `method_rows.csv`: `3DCAF0D642B1A886CB28F0AF5B9582485F2C411FD36E25629CFE45FE45F3F3EE`
- `episode_differences.csv`: `1A29B856618C45C49C564159F3E857D86FE7CE44C3BAAC08CBC2B41B5590CC71`
- `summary.csv`: `BCFD49DBD3E0DAF30C2603F3890DF8BE71E52A8D1CAAB2BE379EA2035C9FD560`

Validation requires 18 registered episodes, 72 method rows, zero failed rows, the complete dataset/shot/seed Cartesian product, and the frozen `NO_GO` verdict. A hash or contract mismatch stops the build.

## Commands

From the repository root:

```powershell
python -m pip install -r source/requirements.txt
python source/work/paper_data.py
python source/audit_candidates.py --final --summary
python source/build_manuscript.py
```

The verifier checks the four archived manuscript candidates in `manuscript/`. The builder writes two regenerated DOCX files to ignored `build/`, leaving the audited copies unchanged. PDF export is kept outside the generator because pagination depends on the installed office renderer.

## Source roles

- `manuscript_content.py` holds the integrated prose, abstract, conclusion, disclosure, and Table IV wording.
- `work/paper_content.py` and `work/icceic_paper_content.py` hold the frozen scientific body and 15 verified references.
- `work/paper_data.py` is the only numerical-data interface.
- `build_manuscript.py` applies the conference template and creates anonymous and author DOCX variants.
- `audit_candidates.py` verifies structure, tables, references, identity separation, metadata, and evidence consistency.
- `render_pdf_pages.py` is an optional visual-inspection helper.

The external editing source and private local project are not redistributed or required.
