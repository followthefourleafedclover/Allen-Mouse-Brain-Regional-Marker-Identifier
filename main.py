import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
import pandas as pd
regions = ['RSP',
 'TEa-PERI-ECT',
 'ACA',
 'AI',
 'SSs-GU-VISC-AIp',
 'AUD',
 'ENT',
 'MOp',
 'MOs_FRP',
 'PAR-POST-PRE-SUB-ProS',
 'PL-ILA-ORB',
 'PTLp',
 'SSp',
 'VIS',
 'VISl',
 'VISm',
 'VISp',
 'HIP']
types = ['1_CR',
 '2_Meis2',
 '3_Meis2',
 '4_Meis2 HPF',
 '5_Lamp5 Lhx6',
 '6_Lamp5 Lhx6',
 '7_Lamp5 Lhx6',
 '8_Lamp5 Lhx6',
 '9_Lamp5 Lhx6',
 '10_Lamp5',
 '11_Lamp5',
 '12_Lamp5',
 '13_Lamp5',
 '14_Lamp5',
 '15_Lamp5',
 '16_Lamp5',
 '17_Lamp5',
 '18_Lamp5',
 '19_Pax6',
 '20_Pax6',
 '21_Sncg',
 '22_Sncg',
 '23_Sncg',
 '24_Sncg',
 '25_Sncg',
 '26_Ntng1 HPF',
 '27_Ntng1 HPF',
 '28_Ntng1 HPF',
 '29_Ntng1 HPF',
 '30_Ntng1 HPF',
 '31_Sncg',
 '32_Sncg',
 '33_Sncg',
 '34_Sncg',
 '35_Sncg',
 '36_Sncg',
 '37_Sncg',
 '38_Sncg',
 '39_Sncg',
 '40_Vip',
 '41_Vip',
 '42_Vip',
 '43_Vip',
 '44_Vip',
 '45_Vip',
 '46_Vip',
 '47_Vip',
 '48_Vip',
 '49_Vip',
 '50_Vip',
 '51_Vip',
 '52_Vip',
 '53_Vip',
 '54_Vip HPF',
 '55_Vip HPF',
 '56_Vip HPF',
 '57_Vip Igfbp6',
 '58_Vip Igfbp6',
 '59_Vip Igfbp6',
 '60_Vip Igfbp6',
 '61_Vip Igfbp6',
 '62_Vip Igfbp6',
 '63_Sst Chodl',
 '64_Sst Chodl',
 '65_Sst Chodl',
 '66_Sst',
 '67_Sst',
 '68_Sst',
 '69_Sst',
 '70_Sst',
 '71_Sst',
 '72_Sst',
 '73_Sst',
 '74_Sst',
 '75_Sst',
 '76_Sst',
 '77_Sst HPF',
 '78_Sst HPF',
 '79_Sst',
 '80_Sst',
 '81_Sst',
 '82_Sst',
 '83_Sst',
 '84_Sst',
 '85_Sst',
 '86_Sst',
 '87_Sst',
 '88_Sst',
 '89_Sst',
 '90_Sst',
 '91_Sst',
 '92_Sst',
 '93_Sst',
 '94_Sst',
 '95_Sst',
 '96_Sst',
 '97_Sst',
 '98_Sst',
 '99_Sst',
 '100_Sst',
 '101_Sst',
 '102_Sst HPF',
 '103_Sst HPF',
 '104_Sst HPF',
 '105_Sst HPF',
 '106_Sst HPF',
 '107_Sst HPF',
 '108_Pvalb',
 '109_Pvalb',
 '110_Pvalb',
 '111_Pvalb',
 '112_Pvalb',
 '113_Pvalb',
 '114_Pvalb',
 '115_Pvalb',
 '116_Pvalb',
 '117_Pvalb',
 '118_Pvalb',
 '119_Pvalb',
 '120_Pvalb',
 '121_Pvalb',
 '122_Pvalb Vipr2',
 '123_Pvalb Vipr2',
 '124_L2 IT APr',
 '125_L2 IT APr',
 '126_L2 IT APr',
 '127_L2 IT APr',
 '128_L2 IT APr',
 '129_L2/3 IT POST-PRE',
 '130_L2/3 IT POST-PRE',
 '131_L2/3 IT POST-PRE',
 '132_L2 IT RSPv-POST-PRE',
 '133_L2 IT RSPv-POST-PRE',
 '134_L2 IT RSP-ACA',
 '135_L3 IT ENTm',
 '136_L3 IT ENTm',
 '137_L3 IT ENTm',
 '138_L3 IT ENTm',
 '139_L3 IT ENTl',
 '140_L3 IT ENTl',
 '141_L2/3 IT PAR',
 '142_L2/3 IT PAR',
 '143_L2/3 IT PAR',
 '144_L2/3 IT PAR',
 '145_L2/3 IT PAR',
 '146_L2 IT ENTm',
 '147_L2 IT ENTm',
 '148_L2 IT ENTm',
 '149_L2 IT ENTm',
 '150_L2 IT ENTm',
 '152_L2/3 IT ENTl',
 '153_L2/3 IT ENTl',
 '154_L2/3 IT ENTl',
 '159_L2/3 IT AI',
 '158_L2/3 IT AI',
 '151_L2 IT ENTl',
 '155_L2/3 IT ENTl',
 '156_L2/3 IT ENTl',
 '157_L2/3 IT ENTl',
 '160_L2/3 IT ENTl',
 '161_L2/3 IT ENTl',
 '162_L2/3 IT CTX',
 '163_L2/3 IT CTX',
 '164_L2/3 IT CTX',
 '165_L2/3 IT CTX',
 '166_L2/3 IT CTX',
 '167_L2/3 IT CTX',
 '168_L2/3 IT CTX',
 '169_L2/3 IT CTX',
 '170_L2/3 IT CTX',
 '171_L2/3 IT CTX',
 '172_L2/3 IT ProS',
 '173_L2/3 IT ProS',
 '174_IT HATA',
 '175_IT HATA',
 '176_IT HATA',
 '177_IT HATA',
 '178_L4 IT CTX',
 '179_L4 IT CTX',
 '180_L4 IT CTX',
 '181_L4 IT CTX',
 '182_L4/5 IT CTX',
 '183_L4/5 IT CTX',
 '184_L4/5 IT CTX',
 '185_L4/5 IT CTX',
 '186_L4/5 IT CTX',
 '187_L4/5 IT CTX',
 '188_L4/5 IT CTX',
 '189_L4/5 IT CTX',
 '190_L4/5 IT CTX',
 '191_L4/5 IT CTX',
 '192_L4/5 IT CTX',
 '193_L4/5 IT CTX',
 '194_L5 IT RSP-ACA',
 '195_L5 IT RSP-ACA',
 '196_L5 IT CTX',
 '197_L5 IT CTX',
 '198_L5 IT CTX',
 '199_L5 IT CTX',
 '200_L5 IT CTX',
 '201_L5 IT CTX',
 '202_L5 IT CTX',
 '203_L5/6 IT CTX',
 '204_L5/6 IT CTX',
 '205_L5/6 IT CTX',
 '206_L5/6 IT CTX',
 '207_L5/6 IT CTX',
 '208_L5/6 IT CTX',
 '209_L5/6 IT CTX',
 '210_L5/6 IT TPE-ENT',
 '211_L5/6 IT TPE-ENT',
 '212_L5/6 IT TPE-ENT',
 '213_L5/6 IT TPE-ENT',
 '214_L5/6 IT PFC',
 '215_L5/6 IT TPE-ENT',
 '216_L5/6 IT TPE-ENT',
 '217_L6 IT CTX',
 '218_L6 IT CTX',
 '219_L6 IT CTX',
 '220_L6 IT CTX',
 '221_L6 IT CTX',
 '222_L6 IT CTX',
 '223_L6 IT CTX',
 '224_L6 IT CTX',
 '225_L6 IT CTX',
 '226_L6 IT CTX',
 '227_L6 IT CTX',
 '228_L6 IT CTX',
 '229_L6 IT CTX',
 '230_L6 IT CTX',
 '231_L6 IT CTX',
 '232_L6 IT CTX',
 '233_L6 IT ENTl',
 '234_L6 IT ENTl',
 '235_L6 IT ENTl',
 '236_Car3',
 '237_Car3',
 '238_Car3',
 '239_L5 PT CTX',
 '240_L5 PT CTX',
 '241_L5 PT CTX',
 '242_L5 PT CTX',
 '243_L5 PT CTX',
 '244_L5 PT CTX',
 '245_L5 PT CTX',
 '246_L5 PT CTX',
 '247_L5 PT CTX',
 '248_L5 PT CTX',
 '249_L5 PT CTX',
 '250_L5 PT CTX',
 '251_L5 PT CTX',
 '252_L5 PT CTX',
 '253_L5 PT CTX',
 '254_L5 PT CTX',
 '255_L5 PT CTX',
 '256_L5 PT CTX',
 '257_L5 PT CTX',
 '258_L5 PT CTX',
 '259_L5 PT CTX',
 '260_L5 PT CTX',
 '261_L4 RSP-ACA',
 '262_L4 RSP-ACA',
 '263_L5 PPP',
 '264_L5/6 NP CTX',
 '265_L5/6 NP CTX',
 '266_L5/6 NP CTX',
 '267_L5/6 NP CTX',
 '268_L5/6 NP CTX',
 '269_L5/6 NP CTX',
 '270_L5/6 NP CT CTX',
 '271_NP SUB',
 '272_NP SUB',
 '273_NP SUB',
 '274_NP SUB',
 '277_NP PPP',
 '275_NP PPP',
 '276_NP PPP',
 '278_L6 CT CTX',
 '279_L6 CT CTX',
 '280_L6 CT CTX',
 '281_L6 CT CTX',
 '282_L6 CT CTX',
 '283_L6 CT CTX',
 '284_L6 CT CTX',
 '285_L6 CT CTX',
 '286_L6 CT CTX',
 '287_L6 CT CTX',
 '288_L6 CT CTX',
 '289_L6 CT CTX',
 '290_L6 CT CTX',
 '291_L6 CT CTX',
 '292_L6 CT CTX',
 '293_L6 CT CTX',
 '294_CT SUB',
 '295_CT SUB',
 '296_CT SUB',
 '297_CT SUB',
 '298_L6 CT ENT',
 '299_L6 CT ENT',
 '308_L6b RHP',
 '300_L6b ENT',
 '301_L6b ENT',
 '302_L6b ENT',
 '303_L6b CTX',
 '304_L6b CTX',
 '305_L6b CTX',
 '306_L6b CTX',
 '307_L6b CTX',
 '310_L6b RHP',
 '309_L6b RHP',
 '311_L6b CTX',
 '312_L6b CTX',
 '313_L6b CTX',
 '314_L6b CTX',
 '315_L6b CTX',
 '316_L6b CTX',
 '317_L6b CTX',
 '318_SUB',
 '319_SUB',
 '320_SUB',
 '321_SUB',
 '322_ProS',
 '325_ProS',
 '323_ProS',
 '324_ProS',
 '326_ProS',
 '327_ProS',
 '328_ProS',
 '329_CA1-ProS',
 '330_CA1-ProS',
 '331_CA1-ProS',
 '332_CA1-ProS',
 '333_CA1-ProS',
 '334_CA1-ve',
 '335_CA1-ve',
 '336_CA1-ve',
 '337_CA1',
 '338_CA1',
 '339_CA1',
 '340_CA1',
 '341_CA1',
 '342_CA1',
 '343_CA1',
 '344_CA1',
 '345_CA1',
 '346_CA1-do',
 '347_CA1-do',
 '348_CA1-do',
 '349_Mossy',
 '350_Mossy',
 '351_CA3-ve',
 '352_CA3-ve',
 '353_CA3-ve',
 '354_CA3-ve',
 '355_CA3-ve',
 '356_CA3-do',
 '357_CA3-do',
 '358_CA3-do',
 '359_CA2-IG-FC',
 '360_CA2-IG-FC',
 '361_DG',
 '362_DG',
 '363_DG',
 '364_DG',
 '365_Oligo',
 '366_Oligo',
 '367_Oligo',
 '368_Oligo',
 '369_Oligo',
 '370_Oligo',
 '371_Oligo',
 '372_Oligo',
 '373_Oligo',
 '374_Oligo',
 '375_Oligo',
 '376_Astro',
 '377_Astro',
 '378_Astro',
 '379_Endo',
 '380_SMC-Peri',
 '382_SMC-Peri',
 '383_VLMC',
 '384_VLMC',
 '385_VLMC',
 '386_Micro-PVM',
 '387_Micro-PVM',
 '388_Micro-PVM']


st.set_page_config(
    page_title="Region Specific Markers"
)
@st.cache_data
def load_data_by_region_and_sex(region, sex_filters):
    # Use pyarrow to load only the relevant region and donor sex directly from Parquet
    metadata = pd.read_parquet(
        'metadata.parquet', 
        filters=[
            ('region_label', '=', region),
            ('donor_sex_label', 'in', sex_filters)
        ], 
        engine='pyarrow'
    )
    return metadata


def make_graph(sample):
    sns.set_theme(style="dark")
    plt.figure(figsize=(12, 8), facecolor='black')  
       
    bar_plot = sns.barplot(x='cluster_label', y='count', data=sample, palette='viridis', edgecolor='black')

     
    plt.title(f'{out}', color='white')
    plt.xlabel('Cell Type', color='white')
    plt.ylabel('Count', color='white')

    
    bar_plot.set_facecolor('black') 
    plt.xticks(color='white') 
    plt.yticks(color='white') 
    plt.xticks(rotation=90)

    for spine in bar_plot.spines.values():
        spine.set_edgecolor('black')  
        spine.set_linewidth(1) 
    st.markdown('### Cell Counts')
    st.pyplot(plt) 
        

#st.title("Region Specific Markers")

filters = ['M', 'F']

with st.sidebar:
    with st.expander(label="Select Region"):
        with st.container(height=200):
            selected_region = st.radio("Choose a region:", options=regions)

    with st.expander(label="Select Filter"):
        selected_filters = {}
        for f in filters:
            selected_filters[f] = st.checkbox(label=f"{f}", value=False)

    submit = st.button(label='Submit', type='primary')

#print(list(selected_filters.items()))
if selected_region and any([x[1] for x in list(selected_filters.items())]) and submit: 
    out = "" 
    filters_opt = [] 
    out += "Region : " + selected_region + " / Filters : "
    for f, is_selected in selected_filters.items():
        if is_selected:
            out += f"{f} "
            filters_opt.append(f)
   #st.write(out)
    with st.spinner('Finding markers'):
        if len(filters_opt) == 2:
            sex_filters = ['M', 'F'] 
        else:
           sex_filters = filters_opt

        
        metadata_filtered = load_data_by_region_and_sex(selected_region, sex_filters)
        sample = metadata_filtered['cluster_label']
        
        total_cells = sample.shape[0]
        print(total_cells)
        sample = sample.value_counts().reset_index().iloc[:30]
        p_values = 0 
        relative_expression_matrix = 0
        make_graph(sample)

        #cells = filtered.index.tolist()
        
        cells = sample['cluster_label'].unique().tolist() 
        markers= []    
        probs = [] 
        columns = types        
        for i in range(len(cells[:5])): 
            data = [] 
            potential_markers = metadata = pd.read_parquet('p_values.parquet', columns=['Feature',cells[i]], engine='pyarrow').sort_values(by=cells[i], ascending=True)
            top_five = potential_markers.iloc[:5]
            
            #st.dataframe(potential_markers)
            #top_marker = potential_markers.iloc[0]['Feature']
            feature_p_val = [] 
            st.header(cells[i])
            st.divider()
            print(top_five)
            for row in top_five.iterrows():
                markers.append((row[-1]['Feature'], row[-1][cells[i]], str(cells[i])))
                data_ = pd.read_parquet(
        'relative_expression_matrix.parquet',
        filters=[('Feature', '=', row[-1]['Feature'])],  # Filter by 'Feature'
        engine='pyarrow'
            ).iloc[0].to_list()[1:-2]
                #print(data_)
                data.append(data_)
                #st.write(f"{row[-1]['Feature']}, p value : {row[-1][cells[i]]}")
                feature_p_val.append((row[-1]['Feature'], row[-1][cells[i]]))

            #print(data)
            index = top_five['Feature'].to_list()
            df = pd.DataFrame(data, columns=columns, index=index)
            sns.set(rc={'axes.facecolor':'black', 'figure.facecolor':'black'})

            plt.figure(figsize=(12, 8))

            plt.gca().set_facecolor('black')

            ax = sns.heatmap(df, cmap='viridis', linewidths=0, cbar=False)

            colorbar = plt.colorbar(ax.collections[0])

            plt.title(f"Relative Expression of the Top Five Most Significant Genes Within {cells[i]}", color='white')
            plt.xlabel("Cell Type", color='white')
            plt.ylabel("Gene (p < 0.05)", color='white')

            plt.xticks(color='white')
            plt.yticks(color='white')
            colorbar.ax.yaxis.set_tick_params(color='white')
            colorbar.outline.set_edgecolor('white')

            plt.setp(colorbar.ax.get_yticklabels(), color='white')

            plt.tight_layout()
            st.pyplot(plt)



        to_arg = [] 
        for marker in markers: 
            feature, p_val, cell = marker 
            z_score = pd.read_parquet(
        'relative_expression_matrix.parquet',
        filters=[('Feature', '=', marker[0])],
        engine='pyarrow'
            )[marker[2]].iloc[0]
            print('z', z_score)
            #print(sample)
            cell_count = sample.loc[sample['cluster_label'] == cell]['count'].iloc[0]
            print('count: ', cell_count, 'total ', total_cells)
            weight =  cell_count / total_cells
            print('w', weight)
            to_arg.append((feature, weight * z_score))
        

        names = [x[0] for x in to_arg]
        weighted_score = [x[1] for x in to_arg]
    
        from collections import defaultdict

        index_dict = defaultdict(list)

        for idx, value in enumerate(names):
            index_dict[value].append(idx)

        duplicates = {key: indexes for key, indexes in index_dict.items() if len(indexes) > 1}

        arg = [] 

        def combine_duplicates(lst):
            combined_dict = {}
            for gene, score in lst:
                if gene in combined_dict:
                    combined_dict[gene] += score
                else:
                    combined_dict[gene] = score

            combined_list = [(gene, score) for gene, score in combined_dict.items()]
            
            return combined_list
        
        arg = combine_duplicates(to_arg)
        arg = [(x[0], round(x[1],4)) for x in arg]
        arg = sorted(arg, key=lambda x: x[1], reverse=True)
        header = ('Gene', 'Aggregated Weighted Relative Expression')

        table = tabulate(arg, header,tablefmt='heavy_outline')
        
        st.divider()
        st.markdown(f"### {selected_region} Specifc Markers")
        st.code(table)
else:
    st.header("Find Region Specific Markers within the Allen Institute for Brain Science: Mouse Whole Cortex and Hippocampus 10x Dataset")
    st.divider()

    col1 ,col2 = st.columns([5, 1])

    with col1: 
        st.metric(label='Genes', value="29,277")

    with col2: 
        st.metric(label='Cell Types', value="387")
    st.write("""Select the options on the sidebar to pick which brain region you want to find markers for, and then select any additional filters. 
             For the most accurate results, select both filters for sex. Please note as of October 2024, neither gene expression data or metadata was avaliable for cell type 381_SMC_Peri.""")
    
    

    st.divider()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1: 
        st.link_button("Visit Allen Brain Map", "https://portal.brain-map.org/")
    with col2: 
        st.link_button("Explore The Mouse Whole Cortex and Hippocampus 10x Dataset", "https://portal.brain-map.org/atlases-and-data/rnaseq/mouse-whole-cortex-and-hippocampus-10x")
    with col3: 
        st.link_button("Read The May 2021 Paper", "https://www.sciencedirect.com/science/article/pii/S0092867421005018?dgcid=rss_sd_all")
