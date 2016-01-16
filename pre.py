"""
Test program for pre-processing schedule
"""
import arrow

base = arrow.now()

def process(raw):
    """
    Line by line processing of syllabus file.  Each line that needs
    processing is preceded by 'head: ' for some string 'head'.  Lines
    may be continued if they don't contain ':'.  
    """
    field = None
    entry = { }
    cooked = [ ] 
    for line in raw:
        line = line.rstrip()
        if len(line) == 0:
            continue
        parts = line.split(':')
        if len(parts) == 1 and field:
            entry[field] = entry[field] + line + " "
            continue
        if len(parts) == 2: 
            field = parts[0]
            content = parts[1]
        else:
            raise ValueError("Trouble with line: '{}'\n".format(line) + 
                "Split into |{}|".format("|".join(parts)))

        if field == "begin":
            try:
                base = arrow.get(content)
            except:
                raise ValueError("Unable to parse date {}".format(content))

        elif field == "week":
            if entry:
                cooked.append(entry)
                entry = { }
            if content.strip(" ") == "1":
                entry['week'] = content + " 1/4/16"
            elif content.strip(" ") == "2":
                entry['week'] = content + " 1/11/16"
            elif content.strip(" ") == "3":
                entry['week'] = content + " 1/18/16"
            elif content.strip(" ") == "4":
                entry['week'] = content + " 1/25/16"
            elif content.strip(" ") == "5":
                entry['week'] = content + " 2/1/16"
            elif content.strip(" ") == "6":
                entry['week'] = content + " 2/8/16"
            elif content.strip(" ") == "7":
                entry['week'] = content + " 2/15/16"
            elif content.strip(" ") == "8":
                entry['week'] = content + " 2/22/16"
            elif content.strip(" ") == "9":
                entry['week'] = content + " 2/29/16"
            elif content.strip(" ") == "10":
                entry['week'] = content + " 3/7/16"
                
            entry['topic'] = ""
            entry['project'] = ""

        elif field == 'topic' or field == 'project':
            entry[field] = content

        else:
            raise ValueError("Syntax error in line: {}".format(line))

    if entry:
        cooked.append(entry)

    return cooked


def main():
    f = open("static/schedule.txt")
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()

    
    
            
    
