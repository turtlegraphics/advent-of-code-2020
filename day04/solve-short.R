library(dplyr)
library(reshape2)
library(tidyr)
library(stringr)
library(readr)

inputpath <- "/Users/bryan/Documents/Puzzles/Advent 2020/day04/input.txt"

# Parse
passports_str <- read_file(inputpath) %>%
  strsplit('\n\n') %>% unlist() %>%
  strsplit('[ \n]') %>%
  melt() %>%
  separate(col = value, into=c('key','value'), sep=':') %>%
  dcast(L1 ~ key, value.var="value") %>%
  select(-L1)

# Re-type variables
passports <- passports_str %>%
  mutate(across(ends_with("yr"), as.integer)) %>%
  mutate(ecl = factor(ecl, levels=c('amb','blu','brn','gry','grn','hzl','oth'))) %>%
  separate(col = hgt, into=c('hgt_v','hgt_u'), sep=-2) %>%
  mutate(hgt_v = as.numeric(hgt_v), hgt_u = factor(hgt_u, levels=c('cm','in'))) %>%
  mutate(hgt_cm = if_else(hgt_u == 'cm', hgt_v, 2.54*hgt_v))

# Filter valid passports
valid <- passports %>%
  filter(1920 <= byr & byr <= 2002) %>%
  filter(2010 <= iyr & iyr <= 2020) %>%
  filter(2020 <= eyr & eyr <= 2030) %>%
  filter( (hgt_u == 'cm' & hgt_v >= 150 & hgt_v <= 193) |
          (hgt_u == 'in' & hgt_v >= 59  & hgt_v <= 76)) %>%
  filter(str_detect(hcl,"^#[0-9a-f]{6}$")) %>%
  filter(!is.na(ecl)) %>%
  filter(str_detect(pid,"^[0-9]{9}$"))

# Count valid passports
print(nrow(valid))
