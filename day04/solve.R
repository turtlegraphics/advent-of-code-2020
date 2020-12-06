library(dplyr)
library(reshape2)
library(tidyr)
library(stringr)

#
aocday <- "04"
#
inputfile <- "input.txt"
# inputfile <- "test.txt"

inputpath <- paste("/Users/bryan/Documents/Puzzles/Advent 2020/day",aocday,"/",inputfile,sep='')

# parsing
# - read file, split into records on \n\n
# - split each record on spaces into key:value pairs,
# - melt away the list structure to produce a tidy data frame with two columns: value and L1
#     value has a string key:value, L1 has the record number of the passport 1,2,3,4... in the file
# - separate the key:value string into two columns
# - cast into a data frame with one row per passport, one column for each key that can appear

passports_str <- read_file(inputpath) %>%
  strsplit('\n\n') %>% unlist() %>%
  strsplit('[ \n]') %>%
  melt() %>%
  separate(col = value, into=c('key','value'), sep=':') %>%
  dcast(L1 ~ key, value.var="value") %>%
  select(-L1)

# data typing
# - convert year variables to integers
# - convert eye color to a factor (conveniently making bad values into NA)
# - split height into hgt_v (value) and hgt_u (units), convert to int and factor

passports <- passports_str %>%
  mutate(across(ends_with("yr"), as.integer)) %>%
  mutate(ecl = factor(ecl, levels=c('amb','blu','brn','gry','grn','hzl','oth'))) %>%
  separate(col = hgt, into=c('hgt_v','hgt_u'), sep=-2) %>%
  mutate(hgt_v = as.numeric(hgt_v), hgt_u = factor(hgt_u, levels=c('cm','in'))) %>%
  mutate(hgt_cm = if_else(hgt_u == 'cm', hgt_v, 2.54*hgt_v))

# filter bad passports

valid <- passports %>%
  filter(1920 <= byr & byr <= 2002) %>%
  filter(2010 <= iyr & iyr <= 2020) %>%
  filter(2020 <= eyr & eyr <= 2030) %>%
  filter( (hgt_u == 'cm' & 150 <= hgt_v & hgt_v <= 193) |
          (hgt_u == 'in' &  59 <= hgt_v & hgt_v <= 76)) %>%
  filter(str_detect(hcl,"^#[0-9a-f]{6}$")) %>%
  filter(!is.na(ecl)) %>%
  filter(str_detect(pid,"^[0-9]{9}$"))

# how many are valid
print(nrow(valid))
