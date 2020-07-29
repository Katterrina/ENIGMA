%% Fetch gene expression data
%    gx          = matrix of gene expression data (82 x 15633)
%    reglabels   = name of cortical regions in same order as gx
%                  (82 x 1 cell array)
%    genelabels  = name of genes in same order as gx
%                  (1 x 15633 cell array)
[gx, reglabels, genelabels] = fetch_ahba();

