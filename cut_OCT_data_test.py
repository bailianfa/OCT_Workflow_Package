from cut_OCT_data_to_indices import cut_OCT_data_to_indices
from read_OCT_bin_files import read_OCT_bin_files
from save_OCT_bin_file import save_OCT_bin_file
from get_indices_of_data_for_visualization import get_indices_of_data_for_visualization
from readGalvoFiles import readGalvoFiles
from filters import filter_galvo_data
import numpy as np
import matplotlib.pyplot as plt

#read galvo file and get indices
galvo_filepath = r'E:\OCT Data\2018-04-25 AutoSection Test Data\Attempt 2\galvo.2d_dbl'
scan_parameters_filepath = r'E:\OCT Data\2018-04-25 AutoSection Test Data\scan_params.txt'
xml_filepath = r'E:\OCT Data\2018-04-25 AutoSection Test Data\12by12.xml'
section_indices = get_indices_of_data_for_visualization(galvo_filepath, scan_parameters_filepath, xml_filepath)

# #plot
# galvo_data = readGalvoFiles(galvo_filepath)[0]
# filtered_galvo = filter_galvo_data(galvo_data, 1500, 12)
#
# plt.figure()
# plt.plot(galvo_data, label='raw')
# plt.plot(filtered_galvo, label='filtered')
# for ind, index_pair in enumerate(section_indices):
#     if ind == 0:
#         plt.plot(range(index_pair[0], index_pair[1]), filtered_galvo[index_pair[0]:index_pair[1]], 'r', linewidth=3, label='autosectioned_indices')
#     else:
#         plt.plot(range(index_pair[0], index_pair[1]), filtered_galvo[index_pair[0]: index_pair[1]], 'r', linewidth=3)
# plt.legend()
# plt.title('Galvo Position Reading vs. Index')
# plt.xlabel('Index')
# plt.ylabel('Galvo Position Reading (mm)')
# plt.show()

#read OCT_file
OCT_bin_filepath = r'E:\OCT Data\2018-04-25 AutoSection Test Data\Attempt 2\9_22_41 AM 4-25-2018\data.bin'
OCT_data = read_OCT_bin_files(OCT_bin_filepath)
mod_OCT_data = cut_OCT_data_to_indices(OCT_data, section_indices)

#check if the same
if np.array_equal(OCT_data[:,section_indices[0][0]:section_indices[0][0]+254], mod_OCT_data[:, 0:254]):
    print(True)
else:
    raise('Blah!')

#save OCT file
OCT_bin_savepath = r'E:\OCT Data\2018-04-25 AutoSection Test Data\Attempt 2\mod_OCT_data\data.bin'
save_OCT_bin_file(mod_OCT_data, OCT_bin_savepath)