
# Dave McEwan 2021-01-05
#
# The keycap is a parameterizable OpenSCAD model with many possible variations.
# CSV files define parameter sets which are read by this Makefile as parallel
# targets using the stardard -j flag.
# STLs are created with machine-readable name first for Makefile simplicity,
# then hardlinked to a human-readable name in the same directory.
#
# To build models of all keycaps into ./stl/
#		make -j8
# The "all" parameter set only includes 1u, 1.5u, 2u.
# If you want more sizes you need to add them to the CSV.
#
# To build models of keycaps of the mcdox layout into ./stl/
#		make CSV=partmodels_mcdox.csv -j8
#
# NOTE: OpenSCAD is missing from Ubuntu18.04 apt repository so AppImage can be
# found from <https://files.openscad.org/OpenSCAD-2019.05-x86_64.AppImage>.

.PHONY: default
default: keycapModels

BUILD ?= ./stl

PARTMODEL_SRC := keycap.scad

CSV ?= partmodels_all.csv
CSV_KEYS := $(shell grep -v "^\w*$$\|^\\\#" $(CSV) | head -n1)
CSV_ROWS := $(shell grep -v "^\w*$$\|^\\\#" $(CSV) | tail -n+2 | sed 's/\s*//g')
N_CSV_KEYS := $(shell echo $(CSV_KEYS) | wc -w)

# Map each row in CSV to a preprocessor define (-D key=value).
# Row selected using the pattern stem variable ($*).
CSV_MAP_DEFINES = \
	for i in $$(seq 1 $(N_CSV_KEYS)); do \
		KEY=$$(echo $(CSV_KEYS) | cut -d' ' -f$$i); \
		VALUE=$$(echo $* | cut -d',' -f$$i); \
		echo -D $$KEY=$$VALUE; \
  done

# Map each row in CSV to a human-readable filename.
# Row selected using the pattern stem variable ($*).
# The AWK table is just an associative array producing nicer names for specific
# parameter values.
# If unknown parameter key/values are used in the CSV then produce key=value.
CSV_MAP_FNAME = \
	fname="keycap"; \
	for i in $$(seq 1 $(N_CSV_KEYS)); do \
		KEY=$$(echo $(CSV_KEYS) | cut -d' ' -f$$i); \
		VALUE=$$(echo $* | cut -d',' -f$$i); \
		fname=$$fname,$$(awk "BEGIN {	\
			shellNum[1] = \"DSA\";        \
			shellNum[2] = \"DCS\";        \
			stemNum[1] = \"CherryMX\";    \
			stemNum[2] = \"MatiasALPS\";  \
			uMul[1]    = \"1u\";          \
			uMul[1.5]  = \"1.5u\";        \
			uMul[2]    = \"2u\";          \
			doBump[0] = \"noBump\";       \
			doBump[1] = \"yesBump\";      \
			print ($$VALUE in $$KEY) ? $$KEY[$$VALUE] : \"$$KEY=$$VALUE\"; \
		}"); \
  done; \
	echo "$$fname.stl"

.PHONY: keycapModels
keycapModels: $(foreach ROW,$(CSV_ROWS),$(BUILD)/$(ROW).stl)
	@echo DONE

$(BUILD)/%.stl: $(PARTMODEL_SRC)
	mkdir -p $(BUILD)/
	./OpenSCAD-2019.05-x86_64.AppImage \
		-o $@ \
		$(shell $(CSV_MAP_DEFINES)) \
		keycap.scad
	ln $@ $(BUILD)/$(shell $(CSV_MAP_FNAME))
