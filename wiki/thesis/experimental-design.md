# Experimental design and reconstruction limits

> Sources: Danielius Vargonas, 2014, thesis sections Medžiagos ir įranga and Eksperimento eiga, tables and appendices; defense presentation
> Raw: [Thesis text](../../raw/thesis/thesis-text.md); [PPTX presentation](../../raw/thesis/presentation-pptx-text.md)
> Updated: 2026-11-19

## Mixture design

Each pH condition compares the same mixture types:

| Sample | Components | Purpose |
|---------|------------|---------|
| A | PpIX | Photosensitizer control |
| B | PpIX and BSA | Protein effect |
| C | PpIX and ascorbic acid | Ascorbate effect |
| D | PpIX, BSA and ascorbic acid | Combined effect |

The source's concentration table gives the following values in mol/l. Decimal commas and exponent spelling are retained to make the transcription checkable.

| Substance | pH 5 (4,9) | pH 7 (6,9) | pH 11 (11,1) |
|-----------|------------|------------|--------------|
| PpIX | 1,25 x 10-4 | 5 x 10-5 | 1,25 x 10-4 |
| BSA, where included | 5 x 10-5 | 10-5 | 5 x 10-5 |
| Ascorbic acid, where included | 5 x 10-3 | 5 x 10-3 | 5 x 10-3 |

A 10-3 mol/l PpIX stock was prepared in DMSO before dilution. The final DMSO fraction is not stated in the extracted methods. Because PpIX and BSA concentrations differ between pH groups, the experiment is not a comparison of pH alone. Both optical absorption and binding equilibria can complicate comparisons of absolute product signals.

## Buffer transcription

The manuscript describes preparation from 0,2 mol/l NaOH and 0,2 mol/l KH2PO4 stocks. Its tables label the following entries as concentrations in mol/l:

| Buffer component | With ascorbic acid: pH 5 / 7 / 11 | Without ascorbic acid: pH 5 / 7 / 11 |
|------------------|--------------------------------|-----------------------------------|
| NaOH | 0,0048 / 0,0291 / 0,04 | 0,06 / 0,0291 / 0,02 |
| KH2PO4 | 0,06 / 0,05 / 0,035 | 0,00035 / 0,05 / 0,02 |

These entries are a historical transcription, not a validated preparation recipe. The acidic condition without ascorbate is particularly in need of checking against laboratory records: the relative listed base and phosphate amounts do not make the nominal acidity self-evident. Buffer composition also changes with ascorbate inclusion, so mixture effects are not isolated from buffer effects. No values have been silently corrected.

## Illumination and readout

The main measurements used an AvaSpec 2048 absorption spectrometer, AvaLight-DHC source and quartz cuvettes with a 2 mm optical path. The manuscript gives a blue LED maximum of 404 nm; the presentation rounds or labels it as 405 nm. Distilled water was used for the reference spectrum. A Perkin Elmer LS55 fluorescence spectrometer is listed among the equipment, but the central reported comparisons are absorption measurements.

The illumination table lists 10 for the acidic condition; 5, 5, 5 for the neutral condition; and 1, 1, 3, 5, 5, 5, 10 for the alkaline condition. The surrounding prose discusses minutes and repeated illumination followed by absorption measurement. It does not fully resolve whether every table entry should be treated as an additional interval or a total elapsed time; reconstruction should retain that ambiguity rather than calculate an assumed cumulative fluence.

No calibrated sample-plane irradiance or delivered fluence is provided in these extracted methods. Time alone cannot establish matched optical dose. The appendix also mentions earlier laser kinetics at 532 nm, while the main pH experiment uses the blue LED. Its caption refers to neutral-medium kinetics but a following caption names pH=11; this additional material has ambiguous condition labeling.

## What cannot be reconstructed

No separate instrument-data archive was supplied. The extracted prose provides no complete independent replicate scheme, uncertainty estimates or statistical analysis for the mixture comparisons. Embedded graph objects remain in the original manuscript and have not been reverse-engineered into numerical datasets. The manuscript's table and figure references permit a qualitative reconstruction, not a validated numerical reanalysis of product yields or reaction rates. A matched buffer/additive reference is not described; the stated reference is distilled water.

## See Also

- [Original research overview](research-overview.md)
- [Findings and proposed mechanisms](findings-and-mechanisms.md)
- [Limitations and open questions](limitations-and-open-questions.md)
- [Proposed continuation research](../research/continuation-research-program.md)
