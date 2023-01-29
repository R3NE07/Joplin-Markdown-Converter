## edit_timestamps.py  
This script extracts the creation and modification date from inside your Markdown files and modifies their metatags accordingly.

<table>
<thead>
  <tr>
    <th colspan="3">Input File</th>
    <th colspan="3">Output File</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Filename</td>
    <td>Created</td>
    <td>Last Modified</td>
    <td>Filename</td>
    <td>Created</td>
    <td>Last Modified</td>
  </tr>
  <tr>
    <td>my_first_note.MD</td>
    <td>01.01.2023 12:04</td>
    <td>01.01.2023 12:04</td>
    <td>my_first_note.MD</td>
    <td>01.02.2022 20:02</td>
    <td>02.02.2022 15:27<br></td>
  </tr>
  <tr>
    <td colspan="3" valign="top">---  <br>title: My First Note  <br>updated: 2022-02-02 15:27:44Z  <br>created: 2022-02-01 08:02:19Z  <br>tags:  <br>  - protocol notes  <br>---  <br><br>This is my first note c:</td>
    <td colspan="3" valign="top">---  <br>title: My First Note  <br>updated: 2022-02-02 15:27:44Z  <br>created: 2022-02-01 08:02:19Z  <br>tags:  <br>  - protocol notes  <br>---  <br><br>This is my first note c:</td>
  </tr>
</tbody>
</table>

---

## delete_timestamp_lines.py  
Searches for the lines starting with `updated:` and `created:` inside the YAML block inside your Markdown files and deletes them.

<table>
<thead>
  <tr>
    <th colspan="3">Input File</th>
    <th colspan="3">Output File</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3" valign="top">---  <br>title: My First Note  <br>updated: 2022-02-02 15:27:44Z  <br>created: 2022-02-01 08:02:19Z  <br>tags:  <br>  - protocol notes  <br>---  <br><br>This is my first note c:</td>
    <td colspan="3" valign="top">---  <br>title: My First Note   <br>tags:  <br>  - protocol notes  <br>---  <br><br>This is my first note c:</td>
  </tr>
</tbody>
</table>

---

## delete_yaml_block.py  
Deletes the entire YAML block inside the markdown files .

<table>
<thead>
  <tr>
    <th colspan="3">Input File</th>
    <th colspan="3">Output File</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3" valign="top">---  <br>title: My First Note   <br>tags:  <br>  - protocol notes  <br>---  <br><br>This is my first note c:</td>
    <td colspan="3" valign="top"><br>This is my first note c:</td>
  </tr>
</tbody>
</table>

---

## delete_first_line.py  
This script deletes the first line of every .MD file.  

<table>
<thead>
  <tr>
    <th colspan="3">Input File</th>
    <th colspan="3">Output File</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3" valign="top"><br>This is my first note c:</td>
    <td colspan="3" valign="top">This is my first note c:</td>
  </tr>
</tbody>
</table>

